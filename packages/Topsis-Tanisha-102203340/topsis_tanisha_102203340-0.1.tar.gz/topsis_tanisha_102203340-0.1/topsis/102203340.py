import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    try:
        df = pd.read_csv(input_file)
        
        if df.shape[1] < 3:
            raise ValueError("Input file must contain at least 3 columns.")
        
        data = df.iloc[:, 1:].values

        try:
            data = data.astype(float)
        except ValueError:
            raise ValueError("Non-numeric values in the input file.")

        weights = np.array([float(w) for w in weights.split(',')])

        print(f"Number of columns in data (excluding the first column): {data.shape[1]}")
        print(f"Number of weights provided: {len(weights)}")
        
        if len(weights) != data.shape[1] or len(impacts.split(',')) != data.shape[1]:
            raise ValueError("The number of weights and impacts must be the same.")

        impacts = [i.strip() for i in impacts.split(',')]
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        impacts = np.array([1 if i == '+' else -1 for i in impacts])

        normalized_data = data / np.sqrt((data**2).sum(axis=0))
        weighted_data = normalized_data * weights

        ideal_best = np.max(weighted_data, axis=0) * (impacts == 1) + np.min(weighted_data, axis=0) * (impacts == -1)
        ideal_worst = np.min(weighted_data, axis=0) * (impacts == 1) + np.max(weighted_data, axis=0) * (impacts == -1)

        edistance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        edistance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

        scores = edistance_worst / (edistance_best + edistance_worst)
        df["Topsis Score"] = scores
        df["Rank"] = df["Topsis Score"].rank(ascending=False, method="dense").astype(int)
        df.to_csv(output_file, index=False)
        
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <script_name>.py <inputFile> <weights> <impacts> <outputFile>")
    else:
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
