import sys
import pandas as pd
import numpy as np


def validate_inputs(input_file, Weights, Impacts):
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    except Exception as e:
        print(f"Error : {e}")
        sys.exit(1)   
    
    if data.shape[1] < 3:
        print("Input file must contain three or more columns.")
        sys.exit(1)

    if not data.iloc[:,1:].select_dtypes(include=[np.number]).shape[1] == data.iloc[:,1:].shape[1]:
        print("From 2nd to last columns must contain numeric values only")
        sys.exit(1)

    weight_list = list(map(float,Weights.split(",")))
    impact_list = Impacts.split(",")

    if len(weight_list) != len(impact_list) or len(weight_list) != data.shape[1]-1:
        print("Number of weights, number of impacts and number of columns must be same.")
        sys.exit(1)
    
    if not all(impact in ["+","-"] for impact in impact_list):
        print("Impacts must be either +ve or -ve.")
        sys.exit(1)
    
    return data, weight_list, impact_list

def topsis(data,Weights,Impacts):
    data_values = data.iloc[:,1:].values.astype(float)
    
    normalized = data_values/np.sqrt((data_values**2).sum(axis=0))

    Weighted = normalized*Weights

    ideal_best = np.max(Weighted,axis=0)*(np.array(Impacts)=='+') + np.min(Weighted,axis=0)*(np.array(Impacts)=='-')
    ideal_worst = np.max(Weighted,axis=0)*(np.array(Impacts)=='-') + np.min(Weighted,axis=0)*(np.array(Impacts)=='+')

    distance_best = np.sqrt(((Weighted-ideal_best)**2).sum(axis=1))
    distance_worst = np.sqrt(((Weighted-ideal_worst)**2).sum(axis=1))

    scores = distance_worst/(distance_best+distance_worst)
    data["Topsis Score"] = scores
    data["Rank"] = pd.Series(scores).rank(ascending=False).astype(int)

    return data


def main():
    if len(sys.argv)!=5:
        print("Usages: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    Weights = sys.argv[2]
    Impacts = sys.argv[3]
    output_file = sys.argv[4]

    data, weight_list, impact_list = validate_inputs(input_file, Weights, Impacts)

    result = topsis(data,weight_list,impact_list)

    try:
        result.to_csv(output_file,index=False)
        print(f"Results saved to : {output_file}")
    except Exception as e:
        print(f"Unable to save the output file.{e}")

if __name__ == "__main__":
    main()




