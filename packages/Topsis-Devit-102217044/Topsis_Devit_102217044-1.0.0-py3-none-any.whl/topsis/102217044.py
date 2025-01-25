import pandas as pd
import numpy as np
import csv
import sys

def main():
    if len(sys.argv) == 5:
        input_file = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        result_file = sys.argv[4]
        topsis(input_file, weights, impacts, result_file)
    else:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 217046-topsis.py 217046-data.csv \"1,1,1,2\" \"+,+,-,+\" 217046-result.csv")

def topsis(input_file, weights, impacts, result_file):
    try:
        df = pd.read_csv(input_file)
        print(df)

        
        if len(weights.split(',')) != len(df.columns) - 1 or len(impacts.split(',')) != len(df.columns) - 1:
            raise ValueError("Number of weights, impacts, and columns must be the same.")


        weights = [float(w.replace('"', '')) for w in weights.split(',')]
        impacts = [1 if i == '+' else 0 for i in impacts.split(',')]

     
        if not df.iloc[:, 1:].applymap(lambda x: isinstance(x, (int, float))).all().all(): # type: ignore
            raise ValueError("Columns from 2nd to last must contain numeric values only.")


        norm_df = df.iloc[:, 1:] / np.sqrt((df.iloc[:, 1:] ** 2).sum())

 
        wt_norm_df = norm_df * weights
        print(wt_norm_df)

   
        ideal_pos = (wt_norm_df.max(axis=0) * np.array(impacts)) + (wt_norm_df.min(axis=0) * (1 - np.array(impacts)))
        ideal_neg = (wt_norm_df.max(axis=0) * (1 - np.array(impacts))) + (wt_norm_df.min(axis=0) * (np.array(impacts)))

       
        sep_pos = ((wt_norm_df - ideal_pos) ** 2).sum(axis=1) ** 0.5
        sep_neg = ((wt_norm_df - ideal_neg) ** 2).sum(axis=1) ** 0.5


        topsis_score = sep_neg / (sep_neg + sep_pos)

     
        rank = topsis_score.rank(ascending=False)

        result_df = pd.concat([df, pd.DataFrame({'Topsis Score': topsis_score, 'Rank': rank})], axis=1)

        result_df.to_csv(result_file, index=False, quoting=csv.QUOTE_ALL, quotechar='"')

        print(f"TOPSIS completed successfully. Result saved to {result_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()