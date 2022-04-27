from reduceAST import reduceAST
from similarity import *
import tqdm
import argparse
import os
import numpy as np
import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_data', type=str, default='test_data_2', help='path to directory')
    parser.add_argument('-c', '--compare', type=str, default='AST_CC', help='algorithm used in comparison ast')

    args = parser.parse_args()
    print('Load file:')
    ast_list = []
    files = sorted(os.listdir(args.input_data))
    files = [f for f in files if f.endswith(".cpp")]
    for file_name in tqdm.tqdm(files):
        file_path = os.path.join(args.input_data, file_name)
        ast_list.append(reduceAST(file_path))

    print('Plagiarism detect:')
    checker = Similarity(args.compare)
    n = len(ast_list)
    res = np.zeros([n, n])
    for i in range(n):
        for j in range(i, n):
            sim = checker.compare(ast_list[i], ast_list[j])
            res[i][j] = sim
            res[j][i] = sim

    # res.tofile('foo.csv', sep=',', format='%10.5f')
    pd.DataFrame(res).to_csv("foo.csv")
    print(res)