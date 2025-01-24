'''
Weighting based on KLI
'''
import scipy.stats as stats
import csv
from collections import Counter
import numpy as np
import time
import argparse
from multiprocessing import Pool
import io

def get_events_and_types(csv_file):
    events = []
    type_dict = Counter()
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            events.append([row['OBJECTID'], row['Type'], row['m_lng'], row['m_lat']])
            type_dict[row['Type']] += 1
    return events, type_dict

def cal_weight(d_list, d):
    w_list = []
    for i in d_list:
        if d == 0:
            w = 1
        else:
            w = np.exp(-0.5 * (i**2/d**2))
        w_list.append(w)
    return w_list

def process_line(line, events, k):
    elements = line.strip().split(';')
    code_counter = Counter()
    weight = Counter()
    if len(elements) >= k+1:
        d = float(elements[k].split(',')[1])
        d_list = [float(element.split(',')[1]) for element in elements[1:k+1]]
        w_list = cal_weight(d_list, d)
        for j, element in enumerate(elements[1:k+1]):
            index = int(element.split(',')[0])
            if index < len(events):
                code = events[index][1]
                code_counter[code] += 1
                weight[code] += w_list[j]
    return [code_counter, weight]

def read_txt(txt_file, events, k, pool_size=4):
    with io.open(txt_file, 'r', encoding='utf-8-sig') as txt:
        lines = txt.readlines()
    with Pool(pool_size) as pool:
        results = pool.starmap(process_line, [(line, events, k) for line in lines])
    return results


'''
Calculate p-value using the hypergeometric distributionParameters:
    N - Total number of elements in the population
    K - Number of elements of interest in the population (successes)
    n - Sample size selected
    k - Minimum number of elements of interest to appear
'''
def cal_p(N, K, n, k):
    p_plus_value = stats.hypergeom.sf(k-1, N, K, n)
    p_minus_value = stats.hypergeom.cdf(k, N, K, n)
    return p_minus_value, p_plus_value

def cal_gwkli_line(k,i, result, events, event_value_dict, total):
    code_counter = result[0]
    weight = result[1]
    w_k = sum(weight.values())
    temp = []
    save_list = events[i]
    if code_counter != Counter():
        for event, value in event_value_dict.items():
            obv = code_counter.get(event, 0)
            w = weight.get(event, 0)
            K1 = event_value_dict[event]
            if save_list[1] == event:
                value -= 1
                K1 -= 1
            p1, p2 = cal_p(total, K1, k, obv)
            if w != 0:
                exp = w_k * (value / total)
                gwkli = w / exp
            else:
                gwkli = 0
            temp.append((gwkli, (p1, p2)))
    else:
        temp = [(0, (1, 1)) for _ in event_value_dict]
    save_list.extend(temp)
    return save_list

def cal_gwkli(k,results, events, event_value_dict, pool_size=4):
    total = sum(event_value_dict.values())-1
    gwkli_list = []
    with Pool(pool_size) as pool:
        gwkli_list = pool.starmap(cal_gwkli_line, [(k,i, result, events, event_value_dict, total) for i, result in enumerate(results)])
    return gwkli_list

def save_csv(results, output_file, event_value_dict):
    headers = ['OBJECTID', 'Type', 'm_lng', 'm_lat'] + list(event_value_dict.keys())
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(results)

def gwkli_csv(txt_file, csv_file, k, output_file):
    start_time = time.time()
    events, type_dict = get_events_and_types(csv_file)
    results = read_txt(txt_file, events, k)
    gwkli_list = cal_gwkli(k,results, events, type_dict)
    save_csv(gwkli_list, output_file, type_dict)
    end_time = time.time()
    print(f"The processing time: {end_time - start_time:.2f}s")
    print(f"The GWKLI is saved to: {output_file}")

def help():
    print("Calculate GWKLI and p-value, save to CSV.")
    print("Arguments:")
    print("gwkli_csv(txt_file, csv_file, k, output_file)")
    print("  <txt_file>  Path to the input txt file.")
    print("  <csv_file>  Path to the input csv file.")
    print("  <output_file>  Path to the output csv file.")
    print("  <k>  Threshold k-nearest neighbor.")
    print("  help  Show this help message and exit.")

def main():
    parser = argparse.ArgumentParser(description='Calculate GWKLI and save to CSV.')
    parser.add_argument('--txt_file', type=str, help='Path to the input txt file.')
    parser.add_argument('--csv_file', type=str, help='Path to the input csv file.')
    parser.add_argument('--k', type=int, help='Threshold k-nearest neighbor.')
    parser.add_argument('--output_file', type=str, help='Path to the output csv file.')
    args = parser.parse_args()
    
    if args.txt_file and args.csv_file and args.k is not None and args.output_file:
        gwkli_csv(args.txt_file, args.csv_file, args.k, args.output_file)
    else:
        help()

if __name__ == '__main__':
    main()