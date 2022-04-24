from compare.lcs import lcs_based_coeff
from compare.ted import ted_similarity
from compare.ast_cc import ast_cc_similarity, ast_cc_compare
from compare.tf_idf import tf_idf_similarity
from reduceAST import traverseAST

# # Sequence Matcher
# from difflib import SequenceMatcher
#
# # Damerau–Levenshtein distance
# import editdistance


# def compare_stats(seq1, seq2):
#     dld = editdistance.eval(seq1, seq2)
#     avg_len = (len(seq1) + len(seq2)) / 2.0
#     # avg_len = max(len(seq1), len(seq2))
#     percent = 1 - (dld / avg_len)
#     return percent, dld


class Similarity:
    def __init__(self, algorithm_compare=None):
        self.function_similarity = ast_cc_compare
        self.algorithm_compare = algorithm_compare
        if algorithm_compare == 'LCS':
            self.function_similarity = lcs_based_coeff
        elif algorithm_compare == 'TED':
            self.function_similarity = ted_similarity
        elif algorithm_compare == 'TF_IDF':
            self.function_similarity = tf_idf_similarity

    def compare(self, ast1, ast2):
        input_1 = ast1
        input_2 = ast2
        if self.algorithm_compare == 'LCS' or self.algorithm_compare == 'TF_IDF':
            input_1 = traverseAST(ast1)
            input_2 = traverseAST(ast2)
        return self.function_similarity(input_1, input_2)
