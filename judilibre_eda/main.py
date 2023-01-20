from pathlib import Path

from matplotlib import pyplot as plt
from nltk.book import Text
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud

from judilibre_eda.corpus import JudilibreCorpusReader

ROOT = Path(__file__).parent
GENERATED_DIR = ROOT.parent / "generated"
from judilibre_eda.collocations import (
    collocation_2,
    collocation_3,
    collocation_4,
    collocation_measure_correlation,
    detailed_collocation_2,
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

    remove_stop_words(judilibre_vocab, stop_words)

    judilibre_vocab.most_common(10)
    judilibre_vocab.most_common(10)
    plot_word_cloud(judilibre_vocab, ROOT / "corpus-wordcloud.png")

    df_result = detailed_collocation_2(
        judilibre_text, judilibre_vocab, stop_words=stop_words, num=30
    )
    print(df_result.to_markdown())

    collocation_2(judilibre_text, method="llr", stop_words=stop_words)
    collocation_2(judilibre_text, method="pmi", stop_words=stop_words)

    collocation_3(judilibre_text, stop_words=stop_words, window_size=3)
    collocation_3(judilibre_text, stop_words=stop_words, window_size=4)

    collocation_4(judilibre_text, stop_words=stop_words, method="llr")
    collocation_4(judilibre_text, stop_words=stop_words, method="pmi")

    collocation_measure_correlation(judilibre_text, stop_words=stop_words)


def remove_stop_words(vocab: FreqDist, stop_words):
    removable_vocab_keys = []
    for vocab_key in vocab.keys():
        if vocab_key.casefold() in stop_words:
            removable_vocab_keys.append(vocab_key)

    for removable_vocab_key in removable_vocab_keys:
        vocab.pop(removable_vocab_key)


def plot_word_cloud(dictionary, plot_path: Path):
    wordcloud = (
        WordCloud(
            background_color="black",
            max_words=150,
            include_numbers=False,
        )
        .generate_from_frequencies(dictionary)
        .recolor(random_state=1)
    )

    # plot the wordcloud
    plt.figure(figsize=(20, 20))
    plt.imshow(wordcloud)

    # to remove the axis value
    plt.axis("off")
    plt.savefig(plot_path)
