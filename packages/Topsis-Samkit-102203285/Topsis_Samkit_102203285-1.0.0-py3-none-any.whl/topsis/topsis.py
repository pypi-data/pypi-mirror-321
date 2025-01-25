import pandas as pd
import numpy as np

class Topsis:
    @staticmethod
    def calculate(input_file, weights, impacts, output_file):
        try:
            # Check file extension and read input file
            if input_file.endswith('.xlsx'):
                data = pd.read_excel(input_file)
            elif input_file.endswith('.csv'):
                data = pd.read_csv(input_file)
            else:
                raise Exception("Unsupported input file format. Please provide a .csv or .xlsx file.")

            # Input file validation
            if data.shape[1] < 3:
                raise Exception("Input file must have at least three columns.")
            if not all(data.iloc[:, 1:].applymap(np.isreal).all()):
                raise Exception("Input file contains non-numeric values.")

            # Convert weights and impacts into lists
            weights = list(map(float, weights.split(',')))
            impacts = impacts.split(',')

            # Validate weights and impacts
            if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
                raise Exception("Number of weights and impacts must match the number of criteria.")
            if not all(i in ['+', '-'] for i in impacts):
                raise Exception("Impacts must be '+' or '-'.")

            # Step 1: Normalize the decision matrix
            normalized_data = data.iloc[:, 1:].div(
                np.sqrt((data.iloc[:, 1:] ** 2).sum()), axis=1
            )

            # Step 2: Apply weights
            weighted_data = normalized_data * weights

            # Step 3: Identify ideal best and ideal worst
            ideal_best = [
                weighted_data[col].max() if impact == '+' else weighted_data[col].min()
                for col, impact in zip(weighted_data.columns, impacts)
            ]
            ideal_worst = [
                weighted_data[col].min() if impact == '+' else weighted_data[col].max()
                for col, impact in zip(weighted_data.columns, impacts)
            ]

            # Step 4: Calculate distances from ideal best and worst
            distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
            distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

            # Step 5: Calculate TOPSIS scores
            scores = distance_worst / (distance_best + distance_worst)
            data['Topsis Score'] = scores
            data['Rank'] = scores.rank(ascending=False).astype(int)

            # Save to output file
            if output_file.endswith('.xlsx'):
                data.to_excel(output_file, index=False)
            elif output_file.endswith('.csv'):
                data.to_csv(output_file, index=False)
            else:
                raise Exception("Unsupported output file format. Please provide a .csv or .xlsx file.")

            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error: {e}")
