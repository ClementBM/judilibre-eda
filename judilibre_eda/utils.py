from nltk.probability import FreqDist


def remove_stop_words(vocab: FreqDist, stop_words):
    removable_vocab_keys = []
    for vocab_key in vocab.keys():
        if vocab_key.casefold() in stop_words:
            removable_vocab_keys.append(vocab_key)

    for removable_vocab_key in removable_vocab_keys:
        vocab.pop(removable_vocab_key)
