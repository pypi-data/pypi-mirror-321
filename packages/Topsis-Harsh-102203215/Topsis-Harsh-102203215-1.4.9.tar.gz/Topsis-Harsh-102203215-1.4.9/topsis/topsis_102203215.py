import numpy as np
import pandas as pd

def topsis(data, weights, impacts):
    """
    Perform TOPSIS ranking on a dataset.

    Parameters:
        data (numpy.ndarray): Decision matrix (alternatives x criteria).
        weights (list or numpy.ndarray): Criteria weights.
        impacts (list): Criteria impacts, '+' for benefit, '-' for cost.

    Returns:
        numpy.ndarray: Ranking of alternatives.
    """
    # Step 1: Validate inputs
    if not isinstance(data, np.ndarray):
        raise ValueError("Data must be a numpy array.")
    if len(weights) != data.shape[1]:
        raise ValueError("Weights length must match the number of criteria.")
    if len(impacts) != data.shape[1]:
        raise ValueError("Impacts length must match the number of criteria.")
    if not all(impact in ['+', '-'] for impact in impacts):
        raise ValueError("Impacts must only contain '+' (benefit) or '-' (cost).")

    # Step 2: Normalize the decision matrix
    norm_data = data / np.sqrt((data**2).sum(axis=0))

    # Step 3: Apply weights to the normalized matrix
    weighted_data = norm_data * weights

    # Step 4: Calculate ideal best and ideal worst values
    def calculate_ideal_values(weighted_data, impacts):
        """
        Calculate the ideal best and ideal worst values for each criterion.

        Parameters:
            weighted_data (numpy.ndarray): Weighted normalized decision matrix.
            impacts (list): List of '+' (benefit) or '-' (cost) for each criterion.

        Returns:
            tuple: Ideal best and ideal worst values as numpy arrays.
        """
        impacts_array = np.array(impacts)  # Convert impacts list to NumPy array
        num_criteria = weighted_data.shape[1]
        ideal_best = np.zeros(num_criteria)
        ideal_worst = np.zeros(num_criteria)

        for i in range(num_criteria):
            if impacts_array[i] == '+':  # Benefit criterion
                ideal_best[i] = np.max(weighted_data[:, i])
                ideal_worst[i] = np.min(weighted_data[:, i])
            elif impacts_array[i] == '-':  # Cost criterion
                ideal_best[i] = np.min(weighted_data[:, i])
                ideal_worst[i] = np.max(weighted_data[:, i])

        return ideal_best, ideal_worst

    ideal_best, ideal_worst = calculate_ideal_values(weighted_data, impacts)

    # Step 5: Calculate distances to the ideal best and worst
    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Step 6: Calculate performance scores
    scores = dist_worst / (dist_best + dist_worst)

    # Step 7: Determine rankings based on scores
    rankings = scores.argsort()[::-1] + 1  # Higher scores get higher ranks

    return rankings, scores


def process_data(input_file, weights, impacts):
    """
    Process the data and perform TOPSIS ranking programmatically.

    Parameters:
        input_file (str): Path to the CSV file containing the decision matrix.
        weights (list): List of weights for each criterion.
        impacts (list): List of impacts ('+' or '-') for each criterion.

    Returns:
        pd.DataFrame: DataFrame containing the original data along with the scores and rankings.
    """
    # Step 1: Read the input CSV file
    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return None

    # Step 2: Extract numeric data (exclude the first column which is assumed to be alternative names)
    if data.shape[1] < 3:
        print("Input file must have at least three columns: alternatives and criteria.")
        return None
    matrix = data.iloc[:, 1:].values  # Get the decision matrix

    # Step 3: Perform TOPSIS
    try:
        rankings, scores = topsis(matrix, weights, impacts)
    except Exception as e:
        print(f"Error during TOPSIS calculation: {e}")
        return None

    # Step 4: Add the rankings and scores to the original data
    data['Score'] = scores
    data['Rank'] = rankings

    return data


