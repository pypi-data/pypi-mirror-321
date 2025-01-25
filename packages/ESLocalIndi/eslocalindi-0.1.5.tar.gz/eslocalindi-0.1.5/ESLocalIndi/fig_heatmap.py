import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse

plt.rcParams['font.sans-serif'] = ['Times New Roman'] 
plt.rcParams['axes.unicode_minus'] = False 

def fig_heatmap(input_file, output_file):
    
    data = pd.read_csv(input_file, index_col=0)
    np.fill_diagonal(data.values, np.nan)  

    labels = [f'C{i+1}' for i in range(data.shape[0])]

    plt.figure(figsize=(12, 9))
    heatmap = sns.heatmap(data, annot=False, cmap='coolwarm', square=True, linewidths=0.5, linecolor='white',
                          xticklabels=labels, yticklabels=labels, cbar_kws={'pad': 0.02})

    ax = plt.gca() 
    ax.tick_params(axis='both', which='both', length=0)

    plt.yticks(rotation=0)
    plt.xticks(fontsize=11, fontweight='bold', fontname='Times New Roman') 
    plt.yticks(fontsize=11, fontweight='bold', fontname='Times New Roman') 

    cbar = heatmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=11, labelcolor='black') 
    cbar.ax.tick_params(axis='y', which='both', labelsize=11) 

    for label in cbar.ax.get_yticklabels():
        label.set_fontname('Times New Roman') 
        label.set_fontweight('bold') 


    plt.rcParams['savefig.dpi'] = 600 
    plt.rcParams['figure.dpi'] = 600 

    plt.savefig(output_file, dpi=600, bbox_inches='tight', transparent=False)
    print(f'Heatmap saved to {output_file}.')

def help():
    print("The local spatial association strength between different crime types is save to jpg.")
    print("Arguments:")
    print("fig_heatmap(input_file, output_file)")
    print("  <input_file>  Path to the local spatial association strength input csv file.")
    print("  <output_file>  Path to the output jpg file.")
    print("  help  Show this help message and exit.")

def main():
    parser = argparse.ArgumentParser(description='Generate a heatmap from the local spatial association strength CSV file.')
    parser.add_argument('--input', required=True, help='Path to the input CSV file.')
    parser.add_argument('--output', required=True, help='Path to save the output image.')
    args = parser.parse_args()
    fig_heatmap(args.input, args.output)

if __name__ == "__main__":
    main()
