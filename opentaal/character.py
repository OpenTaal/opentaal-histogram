"""Class definition for Character."""

from unicodedata import name


class Character():
    """Class for processing characters."""

    @staticmethod
    def get_name(char: str, pretty: bool = False) -> str:
        """Get Unicode name for character.

        :param char: The character for which to get the Unicode name.
        :param pretty: Pretty print in lower case except for names.
        """
        if pretty:
            return name(char).lower().replace('latin ', 'Latin ')
        return name(char)

# pylint:disable=too-many-return-statements

    @staticmethod
    def decode_category(code: str, abbrev: bool = True) -> str:
        """Decode Unicode category code from unicode.category().

        :param code: The two-letter category code.
        :param abbrev: Return abbreveated category seven characters or less.
        :return: The category name.
        """
        first = code[0]
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
        raise ValueError(f'Unsupported Unicode category code {code}')

# pylint:enable=too-many-return-statements

    @staticmethod
    def is_letter(code: str) -> bool:
        """Test if a Unicode category code relates to a letter.

        Note that category code is from unicode.category().

        :param code: The two-character category code.
        :return: True is the category relates to a letter.
        """
        # TODO https://docs.python.org/3/library/stdtypes.html#str.isalpha
        if code in ('LC', 'Ll', 'Lo', 'Lu'):  # excluding Lm: Letter. Modifier
            return True
        return False

    @staticmethod
    def is_letternumeral(code: str) -> bool:
        """Test if a Unicode category code relates to a letter or a numeral.

        Note that category code is from unicode.category().

        :param code: The two-character category code.
        :return: True is the category relates to a letter or numeral.
        """
        # TODO https://docs.python.org/3/library/stdtypes.html#str.isalpha
        if code in ('LC', 'Ll', 'Lo', 'Lu', 'Nd'):
            # excluding Lm: Letter. Modifier
            return True
        return False

    @staticmethod
    def to_hex(character: str, prefix: bool = True, upper: bool = True) -> str:
        """Convert Unicode character to its hexidecimal representation.

        :param character: The character to convert.
        :return: Unicode codepoint in hexidecimal representation.
        """
        tmp = character.encode('utf-8').hex()
        if upper:
            tmp = tmp.upper()
        if prefix:
            tmp = f'U+{tmp}'
        return tmp

    @staticmethod
    def print_friendly(char: str) -> str:  # , markdown=False
        """Make character print friendly.

        :param char: The character to make print friendly.
        :return: Print friendly version of the supplied character.

        See Also
        --------
        - https://en.wikipedia.org/wiki/Whitespace_character
        - https://en.wikipedia.org/wiki/Non-breaking_space
        """
        if char == '\t':  # U+0009 tab character
            return '↹'
        if char == '\n':  # U+000A? new line character
            return '⏎'
        if char == '':  # soft hyphen character
            return '-'
        if char in (' ',  # U+0020 space character
                    ' ',  # U+2007 figure space character
                    ' ',  # U+2008 punctuation space character
                    ' ',  # U+2009 thin space character
                    ' ',  # U+200A hair space character
                    ):
            return '␣'
        if char in (' ',  # U+00A0 no-break space character
                    ' ',  # U+202F narrow no-break space character
                    ):
            return '⍽'
        # if char == '':  # U+???? zero width no-break space character
            # return '␣'
        # if char == ' ':  # U+???? zero width non-joiner character
        #     return ''
        # if char == ' ':  # U+???? zero width joiner character
        #     return ''
        # perhaps escape single quote or backslash or word joiner 2060
        # for identified not implemented  raise ValueError('Unsuode {code}')
        # if char == '|' and markdown:
            # return '\\|' TODO perhaps not needed with `` around it

        return char

    @staticmethod
    def print_friendly_string(text: str) -> str:  # , markdown=False
        """Make string print friendly.

        :param text: The text to make print friendly.
        :return: Print friendly version of the supplied text.

        See Also
        --------
        - https://en.wikipedia.org/wiki/Whitespace_character
        - https://en.wikipedia.org/wiki/Non-breaking_space
        """
        replacements = {
            '\t': '↹',  # U+0009 tab character
            '\n': '⏎',  # U+000A? new line character
            ' ': '␣',  # U+0020 space character
        }
        for src, dst in replacements.items():
            text = text.replace(src, dst)

        # if char == '': # soft hyphen character
        #     return '-'
        #             ' ', # 2007 figure space character
        #             ' ', # 2008 punctuation space character
        #             ' ', # 2009 thin space character
        #             ' ', # 200A hair space character
        #             ):
        #     return '␣'
        # if char in (' ', # 00A0 no-break space character
        #             ' ', # 202F narrow no-break space character
        #             ):
        #     return '⍽'
        # if char == '': # zero width no-break space character
        #     return '␣'
        # if char == ' ': # zero width non-joiner character
        #     return ''
        # if char == ' ': # zero width joiner character
        #     return ''
        # perhaps escape single quote or backslash or word joiner 2060
        # for identified not implemented  raise ValueError('Unsuode {code}')
        # if char == '|' and markdown:
            # return '\\|' TODO perhaps not needed with `` around it

        return text

# TODO localized upper and lower e.g. IJsselmeer
