import numpy as np
import pandas as pd
import argparse


def topsis(data, weights, impacts):
    """
    Function to perform TOPSIS analysis.

    Parameters:
    data (pd.DataFrame): DataFrame containing the decision matrix excluding labels.
    weights (list): List of weights corresponding to each criterion.
    impacts (list): List of '+' for benefit criteria and '-' for cost criteria.

    Returns:
    pd.Series: Ranking scores for each alternative.
    """
    # Step 1: Normalize the Decision Matrix
    normalized_matrix = data / np.sqrt((data**2).sum(axis=0))

    # Step 2: Apply Weights to the Normalized Decision Matrix
    weighted_matrix = normalized_matrix * weights

    # Step 3: Determine Ideal Best and Ideal Worst Values
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(np.max(weighted_matrix.iloc[:, i]))
            ideal_worst.append(np.min(weighted_matrix.iloc[:, i]))
        else:
            ideal_best.append(np.min(weighted_matrix.iloc[:, i]))
            ideal_worst.append(np.max(weighted_matrix.iloc[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Calculate Separation Measures
    separation_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate Relative Closeness to Ideal Solution
    closeness = separation_worst / (separation_best + separation_worst)

    return closeness


def calculate():
    parser = argparse.ArgumentParser(description="TOPSIS Implementation")
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input CSV file (e.g., RollNumber-data.csv)",
    )
    parser.add_argument(
        "weights", type=str, help="Comma-separated weights for criteria (e.g., 1,1,1,2)"
    )
    parser.add_argument(
        "impacts",
        type=str,
        help="Comma-separated impacts for criteria (+ for benefit, - for cost, e.g., +,+,-,+)",
    )
    parser.add_argument(
        "output_file",
        type=str,
        help="Path to save the output CSV file (e.g., RollNumber-result.csv)",
    )

    args = parser.parse_args()

    # Validate input file format
    try:
        data = pd.read_csv(args.input_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
        return
    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    # Check if the input file has at least 3 columns
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        return

    # Validate weights and impacts
    try:
        weights = [float(w) for w in args.weights.split(",")]
    except ValueError:
        print("Error: Weights must be numeric values separated by commas.")
        return

    impacts = args.impacts.split(",")

    if len(weights) != len(data.columns[1:]) or len(impacts) != len(data.columns[1:]):
        print(
            "Error: Number of weights and impacts must match the number of criteria (excluding the first column)."
        )
        return

    if not all(i in ["+", "-"] for i in impacts):
        print("Error: Impacts must be '+' or '-'.")
        return

    # Check if all values (except the first column) are numeric
    try:
        decision_matrix = data.iloc[:, 1:].astype(float)
    except ValueError:
        print("Error: All values from the 2nd to last columns must be numeric.")
        return

    # Perform TOPSIS Analysis
    scores = topsis(decision_matrix, weights, impacts)

    # Append results to the DataFrame
    data["TOPSIS Score"] = scores
    data["Rank"] = data["TOPSIS Score"].rank(ascending=False)

    # Save output to CSV
    try:
        data.to_csv(args.output_file, index=False)
        print(f"Results saved to {args.output_file}")
    except Exception as e:
        print(f"Error saving the output file: {e}")


# if __name__ == "__main__":
#     calculate()
