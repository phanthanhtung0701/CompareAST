from reduceAST import reduceAST
from similarity import *
import tqdm
import argparse
import os
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from itertools import cycle


def get_sim_matrix(input_path, method='AST_CC', save_file=None):
    print('Load file:')
    ast_list = []
    files = sorted(os.listdir(input_path))
    files = [f for f in files if f.endswith(".cpp")]
    for file_name in tqdm.tqdm(files[:17]):
        file_path = os.path.join(args.input_data, file_name)
        ast_list.append(reduceAST(file_path))

    print('Plagiarism detect:')
    checker = Similarity(method)
    n = len(ast_list)
    res = np.zeros([n, n])
    for i in range(n):
        for j in range(i, n):
            sim = checker.compare(ast_list[i], ast_list[j])
            res[i][j] = sim
            res[j][i] = sim

    if save_file:
        pd.DataFrame(res).to_csv(save_file)
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_data', type=str, default='test_data', help='path to directory')
    parser.add_argument('-c', '--compare', type=str, default='LCS', help='algorithm used in comparison ast')

    args = parser.parse_args()
    input_data = args.input_data
    compare = args.compare

    y_true = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    res_ast_cc = get_sim_matrix(input_data, 'AST_CC', save_file='foo_astcc.csv')
    res_lcs = get_sim_matrix(input_data, 'LCS', save_file='foo_lcs.csv')
    res_tf_idf = get_sim_matrix(input_data, 'TF_IDF', save_file='foo_tfidf.csv')

    assert len(y_true) == len(res_ast_cc[0]), "Number label must equal to number result"
    fpr_cc, tpr_cc, thresholds_cc = roc_curve(y_true, res_ast_cc[0], pos_label=1)
    fpr_lcs, tpr_lcs, thresholds_lcs = roc_curve(y_true, res_lcs[0], pos_label=1)
    fpr_tf, tpr_tf, thresholds_tf = roc_curve(y_true, res_tf_idf[0], pos_label=1)

    plt.figure()
    lw = 2
    plt.plot(fpr_cc, tpr_cc, color='darkorange',
             lw=lw, label='ROC curve AST-CC (area = %0.2f)' % auc(fpr_cc, tpr_cc))
    plt.plot(fpr_lcs, tpr_lcs, color='brown',
             lw=lw, label='ROC curve LCS (area = %0.2f)' % auc(fpr_lcs, tpr_lcs))
    plt.plot(fpr_tf, tpr_tf, color='red',
             lw=lw, label='ROC curve TF-IDF (area = %0.2f)' % auc(fpr_tf, tpr_tf))
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.savefig('ROC.jpg')
    plt.show()
