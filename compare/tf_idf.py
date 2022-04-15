# TF-IDF
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


def identityFunction(file):
    return file


def tf_idf_similarity(seq1, seq2, ngram_range=(1, 2)):
    docs = [seq1, seq2]

    VOCAB_LIMIT = 2000  # Can be increased if efficency is not an issue
    vectorizer = TfidfVectorizer(
        analyzer='word',
        tokenizer=identityFunction,
        preprocessor=identityFunction,
        # Consider unigrams and bigrams only
        ngram_range=ngram_range,
        sublinear_tf=True,  # (1+log(tf)) instead of just tf
        max_features=VOCAB_LIMIT,
        encoding="utf-8",
        decode_error="ignore",
        stop_words=None,
        lowercase=False,
        norm="l2"  # Each row will be unit normalized
    )
    S = vectorizer.fit_transform(docs)

    tfm = linear_kernel(S, S)
    return tfm[0][1]
