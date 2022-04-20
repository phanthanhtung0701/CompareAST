from ctokenizer import tokenize
# from sklearn.metrics.pairwise import cosine_similarity
from similarity import *
# position information of longest common subsequence
a = lcs_position("abcd", "cbd")
print(a)