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


# position information of longest common subsequence
a = lcs_position(results1, results2)
# print(a)

# normalized distance between 2 sequences
b = normalized_dist(results1, results2)
print(1 - b)

# print(cosine_similarity(results1, results2))
print(SequenceMatcher(None, results1, results2).ratio())
print(get_pair_stats(results1, results2))