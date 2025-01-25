import pandas as pd
import numpy as np
import sys
import os

def topsis(file_path, weights, impacts, output_file):
    """
    Implements the TOPSIS method for multi-criteria decision making.
    
    Parameters:
    -----------
    file_path : str
        Path to the input CSV file
    weights : list
        List of weights for each criterion
    impacts : list
        List of impacts ('+' or '-') for each criterion
    output_file : str
        Path where the output CSV will be saved
    """
    try:
        # Load data
        data = pd.read_excel(file_path)
        
        # Check if the input data has the required structure
        if len(data.columns) < 3:
            raise ValueError("Input data must have at least 3 columns.")
        
        fund_names = data.iloc[:, 0]
        parameters = data.iloc[:, 1:]
        
        non_numeric_columns = parameters.select_dtypes(exclude=[np.number]).columns
        if len(non_numeric_columns) > 0:
            raise ValueError(
                f"The following columns contain non-numeric values: {', '.join(non_numeric_columns)}. "
                "All criteria columns must contain numeric values only."
            )
        
        # Validate impacts
        valid_impacts = {'+', '-'}
        if not all(i in valid_impacts for i in impacts):
            raise ValueError(
                "Impacts must only contain '+' or '-' separated by commas."
            )
        
        # Validate weights and impacts
        if len(weights) != parameters.shape[1] or len(impacts) != parameters.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of parameters.")
        
        impacts = [1 if i.lower() == 'max' else -1 for i in impacts]
        
        # 1: Normalize the parameters
        normalized = parameters / np.sqrt((parameters**2).sum())
        
        # 2: Weighted normalized decision matrix
        weighted = normalized * weights
        
        # 3: Calculate ideal best and worst
        ideal_best = [weighted.iloc[:, i].max() if impacts[i] == 1 else weighted.iloc[:, i].min() for i in range(len(impacts))]
        ideal_worst = [weighted.iloc[:, i].min() if impacts[i] == 1 else weighted.iloc[:, i].max() for i in range(len(impacts))]
        
        # 4: Calculate distances to ideal best and worst
        distance_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
        distance_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))
        
        # 5: Calculate TOPSIS score
        topsis_score = distance_worst / (distance_best + distance_worst)
        
        # 6: Add results to the dataframe and rank
        data['Topsis Score'] = topsis_score
        data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)
        
        # Save results to the specified output file
        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

        pass
    
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def main():
    """Command line interface for TOPSIS"""
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 102203804.py 102203804-data.csv \"1,1,1,1,1\" \"+, +, -, +, -\" 102203804-result.csv")
        sys.exit(1)
    
    try:
        file_path = sys.argv[1]
        weights = list(map(float, sys.argv[2].split(',')))
        impacts = sys.argv[3].split(',')
        output_file = sys.argv[4]
        
        if not os.path.isfile(file_path):
            raise Exception(f"File {file_path} does not exist")
            
        topsis(file_path, weights, impacts, output_file)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()