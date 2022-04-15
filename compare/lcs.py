# LCS equal to the Levenshtein length
def lcs(X, Y):
    '''
        The function returns the length of the longest common subsequence
        of two sequences X and Y.
        @param X - list of tokens of the first program
        @param Y - list of tokens of the second program
    '''
    m = len(X)
    n = len(Y)

    if m == 0 or n == 0:
        return 0

    # m + 1 rows
    # n + 1 columns
    L = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


def lcs_based_coeff(subseq1, subseq2):
    """The function returns coefficient based on the length
    of the longest common subsequence.
    This coefficient describes how same two sequences.
    @param subseq1 - the first sequence
    @param subseq2 - the second sequnce
    """

    count_elem1 = len(subseq1)
    count_elem2 = len(subseq2)

    if (count_elem1 * count_elem2) == 0:
        return 0.0

    return (2 * lcs(subseq1, subseq2)) / (count_elem1 + count_elem2)