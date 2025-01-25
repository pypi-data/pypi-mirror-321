import sys
import argparse
import numpy as np
import pandas as pd

def validateInputs(input, weights, impacts):
    try:
        data = pd.read_csv(input)
    except FileNotFoundError:
        print(f"Error: The file '{input}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: The input file must have at least 3 columns.")
        sys.exit(1)

    if not data.iloc[:, 1:].apply(lambda col: pd.api.types.is_numeric_dtype(col)).all():
        print("Error: Columns from the 2nd to the last must contain numeric values only.")
        sys.exit(1)



    weights_list = weights.split(",")
    impacts_list = impacts.split(",")

    if len(weights_list) != len(impacts_list) or len(weights_list) != (data.shape[1] - 1):
        print("Error: The number of weights, impacts, and columns (2nd to last) must be the same.")
        sys.exit(1)

    try:
        weights_list = [float(w) for w in weights_list]
    except ValueError:
        print("Error: Weights must be numeric values separated by commas.")
        sys.exit(1)

    if not all(impact in ["+", "-"] for impact in impacts_list):
        print("Error: Impacts must be either '+' or '-' separated by commas.")
        sys.exit(1)

    print("All inputs are valid!")
    return data, weights_list, impacts_list

def topsis(data, weights, impacts):
    if((len(weights) != len(impacts)) or len(weights) != data.shape[1]):
        raise ValueError('Different number of weights, impacts and columns')
    
    normalize = np.sqrt((data ** 2).sum(axis = 0))

    normalizedData = data / normalize

    weightedData = normalizedData * weights

    idealBest = [max(col) if impact == '+' else min(col) for col, impact in zip(weightedData.T, impacts)]
    idealWorst = [min(col) if impact == '+' else max(col) for col, impact in zip(weightedData.T, impacts)]

    SBest = np.sqrt(((weightedData - idealBest) ** 2).sum(axis = 1))
    SWorst = np.sqrt(((weightedData - idealWorst) ** 2).sum(axis = 1))

    score = SWorst / (SBest + SWorst)

    rank = score.argsort()[::-1] + 1

    return score, rank

def readInputFile(input):
    if input.endswith('.csv'):
        df = pd.read_csv(input)
    elif input.endswith('.xlsx') or input.endswith('.xls'):
        df = pd.read_excel(input)
    else:
        raise ValueError('Unsupported file format. Use CSV or XLSX.')
    
    data = df.iloc[:, 1:].values
    alternatives = df.iloc[:, 0].values if df.shape[1] > data.shape[1] else None
    return data, alternatives

def main():
    parser = argparse.ArgumentParser(description = 'Topsis') 
    parser.add_argument('input', help = 'Path to the input CSV file')
    parser.add_argument('weights', help = 'Weights - Comma separated')
    parser.add_argument('impacts', help = 'Impacts(+/-) - Comma Separated')
    parser.add_argument('output', help = 'Path to save the output CSV file')

    args = parser.parse_args()

    data, weights, impacts = validateInputs(args.input, args.weights, args.impacts)

    try:
        data, alternatives = readInputFile(args.input)
    except Exception as e:
        print(f'Error reading input file: {e}')
        return

    weights = np.array(list(map(float, args.weights.split(','))))

    impacts = args.impacts.split(',')

    try:

        score, rank = topsis(data, weights, impacts)

        outputData = np.column_stack((alternatives, data, score, rank)) if alternatives is not None else np.column_stack((data, score, rank))
        columns = ['Alternative'] + [f'Criterion{i+1}' for i in range(data.shape[1])] + ['Score', 'Rank']
        df = pd.DataFrame(outputData, columns=columns)

        if args.output.endswith('.csv'):
            df.to_csv(args.output, index=False)
        elif args.output.endswith('.xlsx'):
            df.to_excel(args.output, index=False)
        print(f'Result saved to {args.output}') 

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "102203234":
    main()