import sys
import os
import pandas  as pd
import numpy as np


def convert_excel_csv(file_input, roll_no):
    try:
        # Check if the input Excel file exists
        if not os.path.exists(file_input):
            raise FileNotFoundError(f"File '{file_input}' not found.")

        # Read the Excel file
        data = pd.read_excel(file_input)

        # Generate the new CSV file name
        file_csv= f"{roll_no}-data.csv"

        # Save the data as a CSV file
        data.to_csv( file_csv, index=False)
        print(f"succesfull and is saved as '{ file_csv}'.")
        return  file_csv

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
def topsis(csvfile_inp, weights, impacts, csvfile_out):
    try:
        data = pd.read_csv(csvfile_inp)

        if len(data.columns) < 3:
            raise ValueError("Input file must contain 3 or more columns.")

        mat1 = data.iloc[:, 1:].values
        if not np.issubdtype(mat1.dtype, np.number):
            raise ValueError("From 2nd to last columns must contain numeric values only.")

        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')

        if len(weights) != mat1.shape[1] or len(impacts) != mat1.shape[1]:
            raise ValueError("keep the no of weights,impacts,col fron 2nd to last col same.")

        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        norm_mat1= mat1 / np.sqrt((mat1 ** 2).sum(axis=0))

        weighted_mat1 = norm_mat1 * weights

        ideal_best = []
        ideal_worst = []
        for i in range(len(impacts)):
            if impacts[i] == '+':
                ideal_best.append(np.max(weighted_mat1[:, i]))
                ideal_worst.append(np.min(weighted_mat1[:, i]))
            else:
                ideal_best.append(np.min(weighted_mat1[:, i]))
                ideal_worst.append(np.max(weighted_mat1[:, i]))

        ideal_best = np.array(ideal_best)
        ideal_worst = np.array(ideal_worst)

        distance_best = np.sqrt(((weighted_mat1 - ideal_best) ** 2).sum(axis=1))
        distance_worst = np.sqrt(((weighted_mat1 - ideal_worst) ** 2).sum(axis=1))

        topsis_score = distance_worst / (distance_best + distance_worst)

        data['Topsis Score'] = topsis_score
        data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)

        file_output = f"{102203818}-result.csv"
        data.to_csv(file_output, index=False)
        print(f"TOPSIS Analysis completed and the results are saved to {file_output}.")

    except FileNotFoundError:
        print(f"Error: File '{input_csv}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    file_input = "data.xlsx"
    roll_no = "102203818"
    weights = '0.2,0.3,0.3,0.1,0.1'
    impacts = '+,+,-,+,-'

     # Convert and rename Excel to CSV
    input_csv = convert_excel_csv(file_input, roll_no)

    topsis(input_csv, weights, impacts, roll_no)