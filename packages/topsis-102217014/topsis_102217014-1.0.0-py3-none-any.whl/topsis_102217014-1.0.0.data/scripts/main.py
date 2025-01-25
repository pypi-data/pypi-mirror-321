import pandas as pd
import numpy as np
from sys import argv

def apply_topsis(inFile: str, weights: str, impacts: str) -> pd.DataFrame:
    input = pd.read_csv(inFile)
    weights: list[float] = [float(i) for i in weights.split(',')]
    impacts: list[str] = impacts.split(',')
    
    if len(weights) != len(impacts) or len(weights) != len(input.columns) - 1:
        print('Input is dimensionally inconsistent')
        raise ValueError
    
    idName = input.columns[0]
    ids = input[idName]
    input.drop(idName, axis=1, inplace=True)

    n = len(input.columns)
    ideal_best = np.zeros(n)
    ideal_worst = np.zeros(n)
    sp = np.zeros(ids.size)
    sn = np.zeros(ids.size)
    score = np.zeros(ids.size)

    for i, col in enumerate(input.columns):
        input[col] /= input[col].sum()**0.5
        if impacts[i] == '-':
            input[col] *= -1 * weights[i]
            ideal_best[i] = min(input[col])
            ideal_worst[i] = max(input[col])
        elif impacts[i] == '+':
            input[col] *= weights[i]
            ideal_best[i] = max(input[col])
            ideal_worst[i] = min(input[col])
        else:
            print(f"Expected + or -, got {impacts[i]}")

    for i in range(ids.size):
        sp[i] = ((np.array(input.loc[i,:]) - ideal_best)**2).sum()
        sn[i] = ((np.array(input.loc[i,:]) - ideal_worst)**2).sum()
        # print(input.loc[i,:].T * ideal_best)
        # sn[i] = input.loc[i,:].T * ideal_worst

    input = pd.concat([ids, input], axis=1)
    input['sp'] = sp
    input['sn'] = sn
    input['topsis_score'] = input['sn'] / (input['sn'] + input['sp'])
    input['rank'] = input['topsis_score'].rank(ascending=False).astype(int)
    return input

if __name__ == '__main__':
    [_, inFile, weights, impacts, outFile] = argv
    apply_topsis(inFile, weights, impacts).to_csv(outFile, index=False)