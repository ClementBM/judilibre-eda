from judilibre_eda.corpus import CorpusReaderBase
from nltk.book import Text
from nltk.collocations import (
    BigramCollocationFinder,
    TrigramCollocationFinder,
    QuadgramCollocationFinder,
    AbstractCollocationFinder,
)
from nltk.metrics import (
    BigramAssocMeasures,
    TrigramAssocMeasures,
    NgramAssocMeasures,
    QuadgramAssocMeasures,
    ranks_from_scores,
    spearman_correlation,
)


def collocation_2(text: Text, method="llr", num=20, window_size=2, stop_words=[]):
    """
    Finds bigram collocations.
    """
    return _collocation_n_grams(
        text=text,
        window_size=window_size,
        collocation_finder=BigramCollocationFinder,
        assoc_measures=BigramAssocMeasures,
        method=method,
        num=num,
        stop_words=stop_words,
    )


def collocation_3(text: Text, method="llr", num=20, window_size=3, stop_words=[]):
    """
    Finds trigram collocations.
    """
    return _collocation_n_grams(
        text=text,
        window_size=window_size,
        collocation_finder=TrigramCollocationFinder,
        assoc_measures=TrigramAssocMeasures,
        method=method,
        num=num,
        stop_words=stop_words,
    )


def collocation_4(text: Text, method="llr", num=20, window_size=4, stop_words=[]):
    """
    Finds quadgram collocations.
    """
    return _collocation_n_grams(
        text=text,
        window_size=window_size,
        collocation_finder=QuadgramCollocationFinder,
        assoc_measures=QuadgramAssocMeasures,
        method=method,
        num=num,
        stop_words=stop_words,
    )


def _collocation_n_grams(
    text: Text,
    window_size: int,
    collocation_finder: AbstractCollocationFinder,
    assoc_measures: NgramAssocMeasures,
    method: str = "llr",
    num: int = 20,
    stop_words=[],
):
    if method == "llr":
        scoring_method = assoc_measures.likelihood_ratio
    elif method == "pmi":
        scoring_method = assoc_measures.pmi
    else:
        raise Exception()

    words = [word.lower() for word in text.tokens]

    colloc_finder = collocation_finder.from_words(words, window_size=window_size)
    colloc_finder.apply_freq_filter(min_freq=2)

    colloc_finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in stop_words)

    likelihood_scores = colloc_finder.score_ngrams(scoring_method)

    collocation_strings = {
        " ".join(colloc): score for colloc, score in likelihood_scores[:num]
    }

    return collocation_strings


def collocation_measure_correlation(
    text: Text,
    collocation_finder: AbstractCollocationFinder = BigramCollocationFinder,
    scoring_method_1=BigramAssocMeasures.likelihood_ratio,
    scoring_method_2=BigramAssocMeasures.pmi,
    stop_words=[],
):
    words = [word.lower() for word in text.tokens]

    colloc_finder = collocation_finder.from_words(words)
    colloc_finder.apply_freq_filter(min_freq=2)

    word_filter = lambda w: len(w) < 3 or w.lower() in stop_words
    colloc_finder.apply_word_filter(word_filter)

    likelihood_ranks = ranks_from_scores(colloc_finder.score_ngrams(scoring_method_1))
    pmi_ranks = ranks_from_scores(colloc_finder.score_ngrams(scoring_method_2))
    correlation = spearman_correlation(likelihood_ranks, pmi_ranks)

    return correlation
