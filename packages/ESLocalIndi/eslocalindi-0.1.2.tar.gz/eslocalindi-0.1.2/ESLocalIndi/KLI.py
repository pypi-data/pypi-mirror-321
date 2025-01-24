'''
Calculate K-Nearest Neighbors
Read the first K elements from each line in the txt file, 
find the corresponding row in the csv file, and count the event types in these rows. 
Then, calculate the relevant indicators and output them to the csv file.
If a row does not contain K elements, 
the corresponding local indicator value for that row is considered statistically insignificant.
'''
import scipy.stats as stats
import pandas as pd
import time
import argparse
from collections import Counter
import io
from multiprocessing import Pool
import csv

def get_events_and_types(csv_file):
    events = []
    type_dict = Counter()
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            events.append([row['OBJECTID'], row['Type'], row['m_lng'], row['m_lat']])
            type_dict[row['Type']] += 1
    return events, type_dict

def process_line(line, events, k):
    elements = line.strip().split(';')
    code_counter = Counter()
    if len(elements) >= k+1:
        for element in elements[1:k+1]:
            index = int(element.split(',')[0])
            if index < len(events):
                code = events[index][1]
                code_counter[code] += 1
    return code_counter

def read_txt(txt_file, events, k,pool_size=4):
    with io.open(txt_file, 'r', encoding='utf-8-sig') as txt:
        lines = txt.readlines()
    with Pool(pool_size) as pool:
        results = pool.starmap(process_line, [(line, events, k) for line in lines])
    return results

def cal_p(N, K, n, k):
    # Calculate the p-value using the hypergeometric distribution
    p_plus_value = stats.hypergeom.sf(k-1, N, K, n)
    p_minus_value = stats.hypergeom.cdf(k, N, K, n)
    return p_minus_value, p_plus_value

def cal_kli_line(k,i,result,events,event_value_dict,total):

    code_counter = result
    temp = []
    save_list = events[i]
    if code_counter != Counter():
        for event, value in event_value_dict.items():
            obv = code_counter.get(event, 0) 
            K1 = event_value_dict[event] 
            if save_list[1] == event:
                value -= 1
                K1 -= 1
            p1, p2 = cal_p(total, K1, k, obv)
            if obv != 0:
                exp = k * (value / total) 
                kli = obv / exp  
            else:
                kli = 0
            temp.append((kli, (p1, p2))) 
    else:
        temp = [(0, (1, 1)) for _ in event_value_dict]
    save_list.extend(temp)
    return save_list

def cal_kli(k,results,events,event_value_dict,pool_size=4):
    total = sum(event_value_dict.values())-1
    kli_list = []
    with Pool(pool_size) as pool:
        kli_list = pool.starmap(cal_kli_line, [(k,i,result,events,event_value_dict,total) for i,result in enumerate(results)])
    return kli_list

def save_csv(results, output_file, event_value_dict):
    headers = ['OBJECTID', 'Type', 'm_lng', 'm_lat'] + list(event_value_dict.keys())
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(results)

def kli_csv(txt_file, csv_file, k, output_file):
    
    start_time = time.time()
    events, type_dict = get_events_and_types(csv_file)
    results = read_txt(txt_file, events, k)
    kli_list = cal_kli(k,results,events, type_dict)
    save_csv(kli_list, output_file, type_dict)
    
    end_time = time.time()
    print(f"The processing time: {end_time - start_time:.2f}s")  
    print(f"The KLI is saved to: {output_file}") 

def help():
    print("Calculate KLI and p-value, save to CSV.")
    print("Arguments:")
    print("kli_csv(txt_file, csv_file, k, output_file)")
    print("  <txt_file>  Path to the input txt file.")
    print("  <csv_file>  Path to the input csv file.")
    print("  <output_file>  Path to the output csv file.")
    print("  <k>  Threshold k-nearest neighbor.")
    print("  help  Show this help message and exit.")

def main():
    # Command-line interface to run the program with arguments
    parser = argparse.ArgumentParser(description='Calculate KLI and save to CSV.')
    parser.add_argument('--txt_file', type=str, help='Path to the input txt file.')
    parser.add_argument('--csv_file', type=str, help='Path to the input csv file.')
    parser.add_argument('--k', type=int, help='Threshold k-nearest neighbor.')
    parser.add_argument('--output_file', type=str, help='Path to the output csv file.')
    args = parser.parse_args()

    if args.txt_file and args.csv_file and args.k is not None and args.output_file:
        kli_csv(args.txt_file, args.csv_file, args.k, args.output_file)
    else:
        help()

if __name__ == '__main__':
    main()

