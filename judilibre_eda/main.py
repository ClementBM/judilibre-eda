from pathlib import Path
from judilibre_eda.corpus import JudilibreCorpusReader
from nltk.book import Text
from nltk.corpus import stopwords
from matplotlib import pyplot as plt

ROOT = Path(__file__).parent
GENERATED_DIR = ROOT.parent / "generated"
from judilibre_eda.collocations import (
    collocation_2,
    collocation_3,
    collocation_4,
    collocation_measure_correlation,
)


def main():
    judilibre_corpus = JudilibreCorpusReader()
    judilibre_text = Text(judilibre_corpus.words())
    stop_words = set(stopwords.words("french"))
    judilibre_vocab = judilibre_text.vocab()

    plt.figure(figsize=(18, 12))
    judilibre_vocab.plot(20, cumulative=False, percents=False, show=False)
    plt.xticks(rotation=45)

    judilibre_text.concordance("notaire")
    judilibre_text.generate(length=10)
    judilibre_text.similar("avocat")

    removable_vocab_keys = []
    for vocab_key in judilibre_vocab.keys():
        if vocab_key.casefold() in stop_words:
            removable_vocab_keys.append(vocab_key)

    for removable_vocab_key in removable_vocab_keys:
        judilibre_vocab.pop(removable_vocab_key)

    judilibre_vocab.most_common(10)

    collocation_2(judilibre_text, method="llr", stop_words=stop_words)
    collocation_2(judilibre_text, method="pmi", stop_words=stop_words)

    collocation_3(judilibre_text, stop_words=stop_words, window_size=3)
    collocation_3(judilibre_text, stop_words=stop_words, window_size=4)
    collocation_4(judilibre_text, stop_words=stop_words)

    collocation_measure_correlation(judilibre_text, stop_words=stop_words)
