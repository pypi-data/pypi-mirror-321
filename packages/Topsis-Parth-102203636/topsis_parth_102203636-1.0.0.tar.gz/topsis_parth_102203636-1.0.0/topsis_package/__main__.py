import sys
import pandas as pd
import numpy as np

def perform_topsis(input_file, weight_values, impact_values, result_file):
    try:
       
        dataset = pd.read_csv(input_file)
        
        if len(dataset.columns) < 3:
            raise ValueError("The input file should have at least three columns.")
        
        weights = [float(w) for w in weight_values.split(',')]
        impacts = impact_values.split(',')
        
        if len(weights) != len(dataset.columns) - 1 or len(impacts) != len(dataset.columns) - 1:
            raise ValueError("The number of weights and impacts must match the number of criteria columns.")

        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-' only.")

        
        dataset.iloc[:, 1:] = dataset.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
        
        if dataset.iloc[:, 1:].isnull().any().any():
            print("Warning: Non-numeric values detected, replacing with 0.")
            dataset.iloc[:, 1:] = dataset.iloc[:, 1:].fillna(0)
        
        decision_matrix = dataset.iloc[:, 1:].values
        norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

        weighted_matrix = norm_matrix * weights

        
        ideal_best = []
        ideal_worst = []
        for i in range(len(impacts)):
            if impacts[i] == '+':
                ideal_best.append(max(weighted_matrix[:, i]))
                ideal_worst.append(min(weighted_matrix[:, i]))
            else:
                ideal_best.append(min(weighted_matrix[:, i]))
                ideal_worst.append(max(weighted_matrix[:, i]))

        
        distance_to_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
        distance_to_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

        
        topsis_scores = distance_to_worst / (distance_to_best + distance_to_worst)

        
        dataset['Topsis Score'] = topsis_scores
        dataset['Rank'] = pd.Series(topsis_scores).rank(ascending=False).astype(int)

        
        dataset.to_csv(result_file, index=False)
        print(f"Results successfully saved to {result_file}")

    except FileNotFoundError:
        print("Error:Input file not found")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 5:
        print('Invalid number of arguments!')
        print("format: python <script.py> <InputFile> <Weights> <Impacts> <ResultFile>")
        return

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    perform_topsis(input_file, weights, impacts, result_file)

if __name__ == "__main__":
    main()
