import argparse
import os
import numpy as np
import pandas as pd
from reduceAST import reduceAST
from similarity import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i_1', '--input_1', type=str, default='test_data_2/test_1.cpp', help='path to directory')
    parser.add_argument('-i_2', '--input_2', type=str, default='test_data_2/test_2.cpp', help='path to directory')
    parser.add_argument('-c', '--compare', type=str, default='AST_CC', help='algorithm used in comparison ast')

    args = parser.parse_args()

    if not (os.path.exists(args.input_1) and os.path.exists(args.input_2)):
        print("File is not exist")
        exit(0)
    ast1 = reduceAST(args.input_1)
    ast2 = reduceAST(args.input_2)

    checker = Similarity(args.compare)
    sim = checker.compare(ast1, ast2)
    print(f'Similarity: {sim}')
