"""Class definition for Checker."""

from functools import lru_cache
from unicodedata import category

import hunspell

from opentaal import Character

# pylint:disable=unspecified-encoding


class Checker():
    """Class for checking spelling.

    Note that methods are cached, hence no methods for add and remove can be
    offered. The maximum cache size has been chosen as a power of two greater
    than the size of the word list.


    See Also
    --------
    - https://pypi.org/project/hunspell/
    - https://github.com/pyhunspell/pyhunspell
    """

    def __init__(self, lang: str = 'nl',
                 path: str = '/usr/share/hunspell/') -> None:
        """TODO.

        :param lang: TODO
        :param path: TODO
        """
        self.__dic: str = f'{path}{lang}.dic'
        self.__aff: str = f'{path}{lang}.aff'
        self.__entries: int = 0
        self.__version: str = ''

        self.__checker = hunspell.HunSpell(self.__dic, self.__aff)

    def __len__(self) -> int:
        """Return the number of entries in the dic file."""
        if self.__entries == 0:
            with open(self.__dic) as file:
                self.__entries = int(file.readline().strip())
        return self.__entries

    def version(self) -> str:
        """Return the verrsion number, date and time of the aff file."""
        if self.__version == '':
            with open(self.__aff) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('# Date and version: '):
                        self.__version = line.split(': ', 1)[1]
                        break
        return self.__version

    def __str__(self) -> str:
        """Return the paths for dic and aff files.

        :return: The paths for dic and aff files.
        """
        return f'{self.__dic} {self.__aff}'

    def __repr__(self) -> str:
        """Return the paths for dic and aff files and their details.

        :return: The paths for dic and aff files and their details.
        """
        return f'dic={self.__dic} entries={len(self)} aff={self.__aff}' \
               f' version={self.version()}'

    @lru_cache(maxsize=524288)
    def check(self, word: str, space: bool = False) -> bool:
        """Check cached spelling of a word.

        :param word: The word to check.
        :param space: Split word on spaces and check all terms.
        :return: True if the word is correctly spelled.
        """
        spelling = self.__checker.spell(word)
        if not spelling and space and ' ' in word:
            spelling = True
            for term in word.split(' '):
                if term != '' and not self.__checker.spell(term):
                    return False
        return spelling

    @lru_cache(maxsize=524288)
    def suggest(self, word: str) -> list:
        """Get cached suggestions for a word, albeit it incorrect or correct.

        :param word: The word to get suggests for.
        :return: TODO.
        """
        return self.__checker.suggest(word)

    @lru_cache(maxsize=524288)
    def analyze(self, word: str) -> list:
        """Get cached analysis for a word.

        :param word: The word to analyze.
        :return: TODO.
        """
        return self.__checker.analyze(word)

    @lru_cache(maxsize=524288)
    def stem(self, word: str) -> list:
        """Get cached stem for a word.

        :param word: The word to stem.
        :return: TODO.
        """
        return self.__checker.stem(word)

    def check_list(self, words: list) -> list:
        """Check spelling of a list of words with result in a list.

        :param words: The list of words to check.
        :return: TODO.
        """
        res = []
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                res.append(True)
            else:
                res.append(self.check(word))
        return res

    def check_list_index(self, words: list) -> set:
        """Check spelling of list of word with result as indeces.

        :param words: The list of words to check.
        :return: TODO.
        """
        res = set()
        index = 0
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                index += 1
                continue
            if not self.check(word):
                res.add(index)
            index += 1
        return res

# pylint:enable=unspecified-encoding
