#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys
from scipy.stats import rankdata

def topsis(input_file, weights, impacts, output_file):
     try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    numeric_df = data.iloc[:, 1:]  # Columns from 2nd to last
    if not numeric_df.select_dtypes(include=['number']).shape[1] == numeric_df.shape[1]:
        print("Error: All columns from 2nd to last must contain numeric values.")

    try:
        weights = np.array([float(w) for w in weights.split(",")])
    except ValueError:
        print("Error: Weights must be numeric and separated by commas.")
        sys.exit(1)

    impacts = impacts.split(",")
    if len(weights) != numeric_df.shape[1] or len(impacts) != numeric_df.shape[1]:
        print("Error: Number of weights and impacts must match the number of numeric columns.")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be '+' or '-'.")
        sys.exit(1)
        
    den = numeric_df.apply(lambda col: np.sqrt((col ** 2).sum()))
    normalized_data = numeric_df.div(den)

    weighted_data = normalized_data * weights

    max_values = weighted_data.apply(lambda col: col.max() if impacts[weighted_data.columns.get_loc(col.name)] == '+' else col.min())
    min_values = weighted_data.apply(lambda col: col.min() if impacts[weighted_data.columns.get_loc(col.name)] == '+' else col.max())

    max_diffs = []
    min_diffs = []

    for _, row in weighted_data.iterrows():
        max_diff = np.sqrt(((max_values - row) ** 2).sum())
        max_diffs.append(max_diff)

        min_diff = np.sqrt(((min_values - row) ** 2).sum())
        min_diffs.append(min_diff)

    max_diffs = np.array(max_diffs)
    min_diffs = np.array(min_diffs)

    Topsis_Score = min_diffs / (max_diffs + min_diffs)
    Topsis_Score = np.nan_to_num(Topsis_Score, nan=0.0)

    ranks = rankdata(-Topsis_Score, method='min')

    data["Topsis_Score"] = Topsis_Score
    data["Rank"] = ranks.astype(int)

    try:
        data.to_csv(output_file, index=False)
        print(f"Results saved to '{output_file}'.")
    except Exception as e:
        print(f"Error saving output file: {e}")
        sys.exit(1)

def main():
  
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    topsis(input_file, weights, impacts, output_file)

   

if __name__ == "__main__":
    main()


# In[ ]:




