import json
import os
from abc import abstractmethod
from pathlib import Path

from nltk.corpus.reader.api import CorpusReader
from nltk.corpus.reader.util import StreamBackedCorpusView, ZipFilePathPointer, concat

from judilibre_eda.tokenizers import JudilibreTokenizer

ROOT = Path(__file__)
JUDILIBRE_JSONL = "dataset.jsonl"


class CorpusReaderBase(CorpusReader):
    @abstractmethod
    def texts(self):
        pass

    @abstractmethod
    def sentences(self):
        pass

    @abstractmethod
    def words(self):
        pass


class JudilibreCorpusReader(CorpusReaderBase):
    corpus_view = StreamBackedCorpusView
    """
    The corpus view class used by this reader.
    """
    _summaries = None

    def __init__(self, word_tokenizer=JudilibreTokenizer(), encoding="utf8"):
        """
        :param word_tokenizer: Tokenizer for breaking the text into
            smaller units, including but not limited to words.
        """

        CorpusReader.__init__(self, str(ROOT.parent), [JUDILIBRE_JSONL], encoding)

        for path in self.abspaths(self._fileids):
            if isinstance(path, ZipFilePathPointer):
                pass
            elif os.path.getsize(path) == 0:
                raise ValueError(f"File {path} is empty")
        """Check that all user-created corpus files are non-empty."""

        self._word_tokenizer = word_tokenizer

    def docs(self, fileids=None):
        """
        Returns the objects
        :return: list of dictionaries deserialised from JSON.
        :rtype: list(dict)
        """
        return concat(
            [
                self.corpus_view(path, self._read_text, encoding=enc)
                for (path, enc, fileid) in self.abspaths(fileids, True, True)
            ]
        )

    def summaries(self):
        """
        Returns only the summaries content
        """
        if self._summaries == None:
            summaries = self.docs()
            standard_summaries = []
            for jsono in summaries:
                text = jsono["summary"]
                if isinstance(text, bytes):
                    text = text.decode(self.encoding)

                standard_summaries.append(text)
            self._summaries = standard_summaries
        return self._summaries

    def texts(self):
        return self.summaries()

    def sentences(self):
        """
        :return: a list of the text content as
            as a list of words.. and punctuation symbols.
        :rtype: list(list(str))
        """
        tokenizer = self._word_tokenizer
        return [tuple(tokenizer.tokenize(t)) for t in self.summaries()]

    def words(self):
        """
        :return: a list of the tokens.
        :rtype: list(str)
        """
        tokens = []
        for title_sentence in self.sentences():
            tokens += title_sentence
        return tokens

    def _read_text(self, stream):
        """
        Assume that each line in stream is a JSON serialised object
        """
        text_array = []
        for i in range(10):
            line = stream.readline()
            if not line:
                return text_array
            text_item = json.loads(line)
            text_array.append(text_item)
        return text_array
