import numpy as np
import pandas as pd
import argparse


def topsisCalc(data,weights,impacts):
    dataCl = data.select_dtypes(include=[np.number]).copy()
    j = 0
    assert len(weights) == len(dataCl.columns), "Error: Length of weights must match number of columns in dataCl"
    assert len(impacts) == len(dataCl.columns), "Error: Length of impacts must match number of columns in dataCl"
    for col in dataCl.columns:
        sumi = 0
        for i in dataCl[col]:
            sumi = sumi+(i*i)
        nor = pow(sumi,(1/2))
        for i in range(len(dataCl[col])):
            dataCl.loc[i,col] = (dataCl.loc[i,col]/nor)*weights[j]
        j = j+1
    
    j = 0
    idealBest = []
    idealWorst = []
    for col in dataCl.columns:
        if(impacts[j]=='+'):
            idealBest.append(max(dataCl[col]))
            idealWorst.append(min(dataCl[col]))
        if(impacts[j] == '-'):
            idealBest.append(min(dataCl[col]))
            idealWorst.append(max(dataCl[col]))
        j=j+1
    
    sibest = []
    siworst = []
    
    for index,row in dataCl.iterrows():
        suma = sum((row[col]-idealBest[k])**2 for k,col in enumerate(dataCl.columns))**0.5
        sumb = sum((row[col] - idealWorst[j]) ** 2 for j, col in enumerate(dataCl.columns)) ** 0.5
        sibest.append(suma)
        siworst.append(sumb)
        
    score = np.array(sibest)/(np.array(sibest)+np.array(siworst))
    resultFile = data.copy()
    resultFile['topsis_scores'] = score
    resultFile['rank'] = score.argsort()[::-1] + 1 
    
    return resultFile

def main():
    parser = argparse.ArgumentParser(description='Run TOPSIS analysis')
    parser.add_argument('input_data_file', help='Path to the input data file (CSV)')
    parser.add_argument('weights', help='Comma-separated list of weights for each criterion')
    parser.add_argument('impacts', help='Comma-separated list of impacts for each criterion (+ or -)')
    parser.add_argument('result_file_name', help='Path to the result file (CSV)')
    
    args = parser.parse_args()

    data = pd.read_excel(args.input_data_file)

    weights = list(map(float, args.weights.split(',')))
    impacts = args.impacts.split(',')

    result = topsisCalc(data, weights, impacts)

    result.to_excel(args.result_file_name, index=False)
    print(f"Results saved to {args.result_file_name}")

if __name__ == '__main__':
    main()
