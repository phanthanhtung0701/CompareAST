from ctokenizer import tokenize
from utils import lcs_position, normalized_dist


file_path1 = 'test_data/test_1.cpp'

# traverse AST
results1 = tokenize(file_path1)
print(results1)

file_path2 = 'test_data/test_2.cpp'

# traverse AST
results2 = tokenize(file_path2)
print(results2)


# position information of longest common subsequence
a = lcs_position(results1, results2)
print(a)

# normalized distance between 2 sequences
b = normalized_dist(results1, results2)

print(b)
