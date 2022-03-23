# LCS
def lcs_position(seq1, seq2):
    """
    Obtain the position information of longest common subsequence.
    Args:
        seq1: A sequence to be iterated.
        seq2: A sequence to be iterated.
    Returns:
        The position information of longest common subsequence.
    """
    m, n = len(seq1), len(seq2)
    # initialize
    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    # fill
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # top first
            if seq1[m - i] == seq2[n - j]:
                dp[i][j] = dp[i - 1][j - 1] + [(m - i, n - j)]
            else:
                # column preference
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], key=len)
    return dp[-1][-1][::-1]


def normalized_dist(seq1, seq2):
    """
    Obtain the normalized distance between two sequences.
    Args:
        seq1: A sequence to be iterated.
        seq2: A sequence to be iterated.
    Returns:
        The normalized distance between two sequences.
    """
    m, n = len(seq1), len(seq2)
    # initialize
    dp = [[i + j for j in range(n + 1)] for i in range(m + 1)]
    # fill
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dist = 1 if seq1[i-1] != seq2[j-1] else 0
            dp[i][j] = min(dp[i-1][j-1] + dist,
                           min(dp[i-1][j], dp[i][j-1]) + 1)
    return dp[-1][-1] / max(m, n)


# Sequence Matcher
from difflib import SequenceMatcher


# Damerau–Levenshtein distance
import editdistance


def compare_stats(seq1, seq2):
    dld = editdistance.eval(seq1, seq2)
    avg_len = (len(seq1) + len(seq2)) / 2.0
    percent = 1 - (dld / avg_len)
    return percent, dld
