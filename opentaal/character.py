'''Class definition for Character.'''

from unicodedata import name

class Character():
    '''Class for creating histograms. See also
    https://en.wikipedia.org/wiki/Histogram ,
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str .'''

    @staticmethod
    def get_name(char: str, pretty: bool=False) -> str:
        '''Get Unicode name for character.

        :param pretty: Pretty print in lower case except for names.'''
        if pretty:
            return name(char).lower().replace('latin ', 'Latin ')
        return name(char)

    @staticmethod
    def decode_category(cat: str, abbrev: bool=True) -> str:  # pylint:disable=too-many-return-statements
        '''Decode Unicode category code from unicode.category().

        :param cat: The two-letter category code.
        :param abbrev: Return abbreveated category name no longer than seven charecters.
        :return: The category name.'''
        first = cat[0]
        if first == 'C':
            return 'control'
        if first == 'L':
            return 'letter'
        if first == 'M':
            return 'mark'
        if first == 'N':
            return 'number'
        if first == 'P':
            if abbrev:
                return 'punct.'
            return 'punctuation'
        if first == 'S':
            return 'symbol'
        if first == 'Z':
            if abbrev:
                return 'whites.'
            return 'whitespace'
        raise ValueError(f'Unsupported Unicode category code {cat}')

    @staticmethod
    def is_letter(cat: str) -> bool:
        '''Test if a Unicode category from unicode.category() code relates to a letter.

        :param cat: The two-character category code.
        :return: True is the category relates to a letter.'''
        #TODO https://docs.python.org/3/library/stdtypes.html#str.isalpha
        if cat in ('LC', 'Ll', 'Lo', 'Lu'): # excluding Lm: Letter. Modifier
            return True
        return False

    @staticmethod
    def to_hex(character: str, prefix: bool=True, upper:bool=True) -> str:
        '''Convert Unicode character to its hexidecimal representation.

        :param character: The character to convert.
        :return: Unicode codepoint in hexidecimal representation.'''
        tmp = character.encode('utf-8').hex()
        if upper:
            tmp = tmp.upper()
        if prefix:
            tmp = f'U+{tmp}'
        return tmp

#TODO localized upper and lower e.g. IJsselmeer