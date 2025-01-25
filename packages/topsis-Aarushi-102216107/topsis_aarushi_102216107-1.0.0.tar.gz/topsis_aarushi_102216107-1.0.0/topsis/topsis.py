import pandas as pd
import numpy as np
import sys
import os

def topsis(inputFileName, weights, impacts, resultFileName):
    try:
        # Check if file exists
        if not os.path.isfile(inputFileName):
            raise FileNotFoundError("Input file not found.")

        # Load the data
        df = pd.read_csv(inputFileName)

        # Validate input file
        if df.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")

        # Extract the data from 2nd to last column
        data = df.iloc[:, 1:].values

        # Check for non-numeric values
        if not np.issubdtype(data.dtype, np.number):
            raise ValueError("From 2nd to last columns, all values must be numeric.")

        # Convert weights and impacts to lists
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        # Check number of weights and impacts
        if len(weights) != data.shape[1]:
            raise ValueError("Number of weights must match the number of columns (from 2nd to last).")
        if len(impacts) != data.shape[1]:
            raise ValueError("Number of impacts must match the number of columns (from 2nd to last).")

        # Check for valid impacts
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Step 1: Normalize the decision matrix
        norm_matrix = data / np.sqrt((data ** 2).sum(axis=0))

        # Step 2: Multiply by weights
        weighted_matrix = norm_matrix * weights

        # Step 3: Determine ideal best and worst values
        ideal_best = np.max(weighted_matrix, axis=0) * (np.array(impacts) == '+') + \
                     np.min(weighted_matrix, axis=0) * (np.array(impacts) == '-')
        ideal_worst = np.min(weighted_matrix, axis=0) * (np.array(impacts) == '+') + \
                      np.max(weighted_matrix, axis=0) * (np.array(impacts) == '-')

        # Step 4: Calculate distances from ideal best and worst
        distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

        # Step 5: Calculate TOPSIS score
        topsis_score = distance_worst / (distance_best + distance_worst)

        # Add TOPSIS score and rank to dataframe
        df['Topsis Score'] = topsis_score
        df['Rank'] = topsis_score.rank(ascending=False).astype(int)

        # Save the results to a new CSV file
        df.to_csv(resultFileName, index=False)
        print(f"Results saved to {resultFileName}.")

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
