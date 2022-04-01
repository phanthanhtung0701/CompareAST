from ctokenizer import tokenize
# from sklearn.metrics.pairwise import cosine_similarity
from similarity import *


file_path1 = 'test_data/00-original.cpp'

# traverse AST
results1 = tokenize(file_path1)
# print(results1)

file_path2 = 'test_data/02-order-changed.cpp'

# traverse AST
results2 = tokenize(file_path2)
# print(results2)


# normalized distance between 2 sequences
print('---LCS\t\t\t\t\t: ', end='')
print(lcs_based_coeff(results1, results2))


print('---Sequence Matcher\t\t: ', end='')
print(SequenceMatcher(None, results1, results2).ratio())

print('---Damerau–Levenshtein\t: ', end='')
print(compare_stats(results1, results2)[0])

print('---TF_IDF\t\t\t\t: ', end='')
print(tf_idf_similarity(results1, results2)[0][1])