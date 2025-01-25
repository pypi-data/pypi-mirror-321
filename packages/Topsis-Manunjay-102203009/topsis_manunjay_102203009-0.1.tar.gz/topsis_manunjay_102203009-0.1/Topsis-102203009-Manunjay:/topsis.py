import pandas as pd
import numpy as np
import sys

# Function to normalize the decision matrix
def normalize_matrix(matrix):
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
    return norm_matrix

# Function to calculate the weighted matrix
def weighted_matrix(norm_matrix, weights):
    # Ensure the weights are converted to a numpy array for element-wise multiplication
    weights = np.array(weights)
    weighted_matrix = norm_matrix * weights
    return weighted_matrix

# Function to calculate the ideal solution (maximum for positive, minimum for negative criteria)
def ideal_solution(weighted_matrix, impacts):
    ideal = []
    for i in range(weighted_matrix.shape[1]):
        if impacts[i] == '+':
            ideal.append(weighted_matrix.iloc[:, i].max())  # Maximum for positive impacts
        else:
            ideal.append(weighted_matrix.iloc[:, i].min())  # Minimum for negative impacts
    return ideal

# Function to calculate the negative ideal solution
def negative_ideal_solution(weighted_matrix, impacts):
    negative_ideal = []
    for i in range(weighted_matrix.shape[1]):
        if impacts[i] == '+':
            negative_ideal.append(weighted_matrix.iloc[:, i].min())  # Minimum for positive impacts
        else:
            negative_ideal.append(weighted_matrix.iloc[:, i].max())  # Maximum for negative impacts
    return negative_ideal

# Function to calculate the Topsis score
def topsis_score(weighted_matrix, ideal_solution, negative_ideal_solution):
    # Calculate the Euclidean distance from the ideal and negative ideal solutions
    distance_from_ideal = np.sqrt(((weighted_matrix - ideal_solution) ** 2).sum(axis=1))
    distance_from_negative_ideal = np.sqrt(((weighted_matrix - negative_ideal_solution) ** 2).sum(axis=1))

    # Calculate the Topsis score
    score = distance_from_negative_ideal / (distance_from_ideal + distance_from_negative_ideal)
    return score

# Function to rank the alternatives based on Topsis score
def rank(scores):
    return np.argsort(scores)[::-1] + 1  # Ranks in descending order (higher score = better rank)

# Main function to handle the command line interface and Topsis method
def main():
    # Get arguments from command line
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3]
    result_file = sys.argv[4]

    try:
        # Read the input file
        df = pd.read_csv(input_file)

        # Check the number of columns and ensure the number of weights and impacts match
        num_columns = df.shape[1] - 1  # excluding the first "Object" column
        weights = list(map(float, weights_str.split(',')))  # Convert weights to a list of floats
        impacts = impacts_str.split(',')  # Convert impacts to a list of strings

        # Ensure the number of weights and impacts match the number of criteria columns
        if len(weights) != num_columns or len(impacts) != num_columns:
            raise ValueError("Number of weights and impacts must match the number of criteria columns.")

        # Check if all columns (except the first) contain numeric values
        if not df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').notna().all().all():
            raise ValueError("All numeric columns must contain valid numbers.")

        # Normalize the matrix (excluding the "Object" column)
        norm_matrix = normalize_matrix(df.iloc[:, 1:])  # Exclude the "Object" column

        # Calculate the weighted matrix
        weighted_matrix_result = weighted_matrix(norm_matrix, weights)

        # Calculate the ideal and negative ideal solutions
        ideal_solution_result = ideal_solution(weighted_matrix_result, impacts)
        negative_ideal_solution_result = negative_ideal_solution(weighted_matrix_result, impacts)

        # Calculate the Topsis score
        topsis_scores = topsis_score(weighted_matrix_result, ideal_solution_result, negative_ideal_solution_result)

        # Calculate the ranks based on Topsis score
        ranks = rank(topsis_scores)

        # Add the Topsis score and rank to the dataframe
        df['Topsis Score'] = topsis_scores
        df['Rank'] = ranks

        # Save the result to a CSV file
        df.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Execute the main function
if __name__ == "__main__":
    main()
