import pandas as pd
import numpy as np
import sys

# Function to validate weights and impacts
def validate_weights_and_impacts(weights, impacts, num_criteria):
    try:
        weights = list(map(float, weights.split(',')))
    except ValueError:
        raise ValueError("Weights must be numeric values separated by commas.")

    impacts = impacts.split(',')
    if len(weights) != num_criteria or len(impacts) != num_criteria:
        raise ValueError("Number of weights and impacts must match the number of criteria.")

    if not all(impact in ['+', '-'] for impact in impacts):
        raise ValueError("Impacts must be '+' or '-'.")

    return weights, impacts

# Function to normalize the dataset
def normalize_dataset(df, criteria_columns):
    for column in criteria_columns:
        column_values = df[column]
        norm = np.sqrt((column_values**2).sum())
        df[column] = column_values / norm
    return df

# Function to calculate Topsis scores
def calculate_topsis(df, weights, impacts, criteria_columns):
    weighted_df = df[criteria_columns].copy()

    # Applying weights
    for i, column in enumerate(criteria_columns):
        weighted_df[column] *= weights[i]

    # Identifying ideal best and worst values
    ideal_best = [weighted_df[column].max() if impacts[i] == '+' else weighted_df[column].min() for i, column in enumerate(criteria_columns)]
    ideal_worst = [weighted_df[column].min() if impacts[i] == '+' else weighted_df[column].max() for i, column in enumerate(criteria_columns)]

    # Calculating distances to ideal best and worst
    distance_to_best = np.sqrt(((weighted_df - ideal_best) ** 2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_df - ideal_worst) ** 2).sum(axis=1))

    # Calculating Topsis score
    topsis_score = distance_to_worst / (distance_to_best + distance_to_worst)

    # Adding Topsis score and rank to the original DataFrame
    df['Topsis_Score'] = topsis_score
    df['Rank'] = topsis_score.rank(ascending=False, method='min')
    return df

# Main function
def main():
    if len(sys.argv) != 5:
        print("Usages: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file, weights, impacts, result_file = sys.argv[1:]

    try:
        # Reading the input file
        df = pd.read_csv(input_file)

        # Validating input file format
        if len(df.columns) < 3:
            raise ValueError("Input file must contain at least three columns.")

        criteria_columns = df.columns[1:]
        if not all(pd.api.types.is_numeric_dtype(df[column]) for column in criteria_columns):
            raise ValueError("From 2nd to last columns, all values must be numeric.")

        # Validating weights and impacts
        weights, impacts = validate_weights_and_impacts(weights, impacts, len(criteria_columns))

        # Normalizing the dataset
        df_normalized = normalize_dataset(df.copy(), criteria_columns)

        # Calculating Topsis scores
        result_df = calculate_topsis(df_normalized, weights, impacts, criteria_columns)

        # Writing result to the output file
        final_columns = list(df.columns[:len(criteria_columns) + 1]) + ['Topsis_Score', 'Rank']
        result_df[final_columns].to_csv(result_file, index=False)
        print(f"Topsis result has been successfully written to {result_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
