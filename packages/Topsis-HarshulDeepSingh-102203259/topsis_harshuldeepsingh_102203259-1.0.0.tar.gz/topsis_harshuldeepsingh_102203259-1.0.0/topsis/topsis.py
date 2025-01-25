import sys
import pandas as pd
import numpy as np

def validate_inputs(args):
    if len(args) != 5:
        raise ValueError("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")

    input_file = args[1]
    weights = args[2]
    impacts = args[3]
    output_file = args[4]

    # Check if weights and impacts are properly formatted
    try:
        weights = list(map(float, weights.split(',')))
    except ValueError:
        raise ValueError("Weights must be numeric and separated by commas.")

    impacts = impacts.split(',')
    if not all(i in ['+', '-'] for i in impacts):
        raise ValueError("Impacts must be either '+' or '-'.")

    return input_file, weights, impacts, output_file

def read_input_file(file_name):
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_name}")

    if len(df.columns) < 3:
        raise ValueError("Input file must contain at least three columns.")

    if not np.issubdtype(df.iloc[:, 1:].dtypes.values[0], np.number):
        raise ValueError("All columns except the first must contain numeric values.")

    return df

def normalize_decision_matrix(df):
    numeric_data = df.iloc[:, 1:]
    norm_data = numeric_data / np.sqrt((numeric_data**2).sum(axis=0))
    return norm_data

def calculate_topsis(df, weights, impacts):
    norm_data = normalize_decision_matrix(df)

    # Apply weights
    weighted_data = norm_data * weights

    # Determine ideal best and worst values
    ideal_best = np.where(np.array(impacts) == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(np.array(impacts) == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))

    # Calculate distances
    distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate Topsis score
    topsis_score = distance_worst / (distance_best + distance_worst)

    # Add scores and ranks to the DataFrame
    df['Topsis Score'] = topsis_score
    df['Rank'] = topsis_score.rank(ascending=False).astype(int)

    return df

def main():
    try:
        # Validate input arguments
        input_file, weights, impacts, output_file = validate_inputs(sys.argv)

        # Read and validate input file
        df = read_input_file(input_file)

        # Ensure weights and impacts match the number of columns (excluding the first column)
        if len(weights) != df.shape[1] - 1 or len(impacts) != df.shape[1] - 1:
            raise ValueError("Number of weights, impacts, and numeric columns must be the same.")

        # Perform Topsis calculation
        result_df = calculate_topsis(df, weights, impacts)

        # Write the result to the output file
        result_df.to_csv(output_file, index=False)
        print(f"Topsis analysis completed. Results saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
