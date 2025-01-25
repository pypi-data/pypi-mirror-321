'''
Calculate the K value for each row of elements based on the distance threshold. The idea here is similar to K-nearest neighbors; 
however, in the KSR calculation, the K elements in each row are equal, while in DLI, the K value is different for each row.

Read the first K elements from each line of the txt file, find the corresponding row in the csv file, and count the event types in these rows. 
Then, compute the relevant indicators and output them to the csv file.

If a row does not contain K elements, the corresponding local indicator value for that row is considered statistically insignificant.
'''
import pandas as pd
import csv
import time
import argparse
from scipy.stats import hypergeom
from collections import Counter
import io
from multiprocessing import Pool

def get_events_and_types(csv_file):
    events = []
    type_dict = Counter()
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            events.append([row['OBJECTID'], row['Type'], row['m_lng'], row['m_lat']])
            type_dict[row['Type']] += 1
    return events, type_dict

def process_line(line, events, d):
    elements = line.strip().split(';')
    k = 0
    if len(elements) > 1:
        for element in elements[1:]:
            dis = float(element.split(',')[1])
            if dis < d:
                k += 1
    code_counter = Counter()
    if len(elements) > k+1:
        for element in elements[1:k + 1]:
            index = int(element.split(',')[0])
            if index < len(events):
                code = events[index][1]
                code_counter[code] += 1
    return [code_counter, k]

def read_txt(txt_file, events, d, pool_size=4):
    with io.open(txt_file, 'r', encoding='utf-8-sig') as txt:
        lines = txt.readlines()
    with Pool(pool_size) as pool:
        results = pool.starmap(process_line, [(line, events, d) for line in lines])
    return results


def cal_p(N, K, n, k):
    p_plus_value = hypergeom.sf(k - 1, N, K, n)
    p_minus_value = hypergeom.cdf(k, N, K, n)
    return p_minus_value, p_plus_value

def cal_dli_line(i, result, events, event_value_dict, total):
    code_counter = result[0]
    k = result[1]
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
            exp = k * (value / total) if obv != 0 else 0
            dli = obv / exp if exp != 0 else 0
            temp.append((dli, (p1, p2)))
    else:
        temp = [(0, (1, 1)) for _ in event_value_dict]
    save_list.extend(temp)
    return save_list


def cal_dli(results,events,event_value_dict,pool_size=4):
    total = sum(event_value_dict.values()) - 1
    dli_list = []
    with Pool(pool_size) as pool:
        dli_list = pool.starmap(cal_dli_line, [(i, result, events, event_value_dict, total) for i, result in enumerate(results)])
    return dli_list

def save_csv(results, output_file, event_value_dict):
    headers = ['OBJECTID', 'Type', 'm_lng', 'm_lat'] + list(event_value_dict.keys())
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(results)

def dli_csv(txt_file, csv_file, d, output_file):
    start_time = time.time()
    events, type_dict = get_events_and_types(csv_file)
    results = read_txt(txt_file, events, d)
    dli_list = cal_dli(results, events, type_dict)
    save_csv(dli_list, output_file, type_dict)
    end_time = time.time()
    print(f"Processing time: {end_time - start_time:.2f}s")
    print(f"The DLI is saved to: {output_file}")

def help():
    print("Calculate DLI and p-value, save to CSV.")
    print("Arguments:")
    print("dli_csv(txt_file, csv_file, d, output_file)")
    print("  <txt_file>  Path to the input txt file.")
    print("  <csv_file>  Path to the input csv file.")
    print("  <output_file>  Path to the output csv file.")
    print("  <d>  Threshold distance.")
    print("  help  Show this help message and exit.")

def main():
    parser = argparse.ArgumentParser(description='Calculate DLI and save as a CSV file.')
    parser.add_argument('--txt_file', type=str, required=True, help='Path to the input txt file.')
    parser.add_argument('--csv_file', type=str, required=True, help='Path to the input csv file.')
    parser.add_argument('--d', type=float, required=True, help='Threshold distance.')
    parser.add_argument('--output_file', type=str, required=True, help='Path to the output csv file.')
    args = parser.parse_args()

    if args.txt_file and args.csv_file and args.d is not None and args.output_file:
        dli_csv(args.txt_file, args.csv_file, args.d, args.output_file)
    else:
        help()
    
if __name__ == '__main__':
    main()
