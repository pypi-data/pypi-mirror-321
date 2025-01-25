import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Convert all relevant columns to numeric, ignoring errors (converts non-numeric values to NaN)
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Handle NaN values: For simplicity, we'll drop rows with NaN values
    df = df.dropna()

    # Normalize the decision matrix
    normalized_matrix = pd.DataFrame()
    for col in df.columns[1:]:  # Skip 'Fund Name' column
        normalized_matrix[col] = df[col] / np.sqrt((df[col]**2).sum())

    # Apply weights
    weights = list(map(float, weights.split(',')))
    weighted_matrix = normalized_matrix * weights

    # Determine the ideal and negative-ideal solutions
    ideal_solution = []
    negative_ideal_solution = []
    
    for i, impact in enumerate(impacts.split(',')):
        if impact == "+":
            ideal_solution.append(weighted_matrix.iloc[:, i].max())
            negative_ideal_solution.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_solution.append(weighted_matrix.iloc[:, i].min())
            negative_ideal_solution.append(weighted_matrix.iloc[:, i].max())

    # Calculate the Euclidean distance for each alternative from the ideal and negative-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_matrix - ideal_solution) ** 2).sum(axis=1))
    distance_to_negative_ideal = np.sqrt(((weighted_matrix - negative_ideal_solution) ** 2).sum(axis=1))

    # Calculate the relative closeness to the ideal solution
    relative_closeness = distance_to_negative_ideal / (distance_to_ideal + distance_to_negative_ideal)

    # Rank the alternatives based on the relative closeness
    df['Rank'] = relative_closeness.rank(ascending=False)

    # Save the results to the output file
    df.to_csv(output_file, index=False)

def main(input_file, weights, impacts, output_file):
    topsis(input_file, weights, impacts, output_file)
