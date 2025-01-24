"""
emoji.tokenizer
~~~~~~~~~~~~~~~

Components for detecting and tokenizing Swahili emoji in strings.

"""

from typing import List, Dict, Iterator, Union, Any

__all__ = [
    'EmojiMatch',
    'Token',
    'tokenize',
    'filter_tokens',
]

_SEARCH_TREE: Dict[str, Any] = {}


class EmojiMatch:
    """
    Represents a match of an emoji in a string.
    """

    __slots__ = ('emoji', 'start', 'end', 'data')

    def __init__(self, emoji: str, start: int, end: int, data: Union[Dict[str, Any], None]):
        self.emoji = emoji
        """The emoji substring"""

        self.start = start
        """The start index of the match in the string"""

        self.end = end
        """The end index of the match in the string"""

        self.data = data
        """The entry from :data:`EMOJI_DATA` for this emoji or `None` if not found"""

    def __repr__(self) -> str:
        return f'EmojiMatch({self.emoji}, {self.start}:{self.end})'


class Token:
    """
    A container for matched emoji or plain text characters.
    """

    def __init__(self, chars: str, value: Union[str, EmojiMatch]):
        self.chars = chars
        self.value = value

    def __repr__(self) -> str:
        return f'Token({self.chars}, {self.value})'


def tokenize(string: str) -> Iterator[Token]:
    """
    Tokenizes a string, detecting emoji and yielding them as `Token` objects.

    :param string: The input string to tokenize.
    :return: An iterator over `Token` objects for each emoji or character in the string.
    """
    tree = get_search_tree()
    result: List[Token] = []
    i = 0
    length = len(string)

    while i < length:
        char = string[i]
        if char in tree:
            sub_tree = tree[char]
            j = i + 1
            while j < length and string[j] in sub_tree:
                sub_tree = sub_tree[string[j]]
                j += 1
            if 'data' in sub_tree:
                match_data = sub_tree['data']
                result.append(Token(string[i:j], EmojiMatch(string[i:j], i, j, match_data)))
                i = j
                continue

        # If not emoji, add as plain text
        result.append(Token(char, char))
        i += 1

    yield from result


def filter_tokens(matches: Iterator[Token], emoji_only: bool = False) -> Iterator[Token]:
    """
    Filters tokens, optionally yielding only emoji.

    :param matches: An iterator over `Token` objects.
    :param emoji_only: If True, only yield tokens containing emoji.
    :return: Filtered iterator of tokens.
    """
    for token in matches:
        if emoji_only and isinstance(token.value, EmojiMatch):
            yield token
        elif not emoji_only:
            yield token


def get_search_tree() -> Dict[str, Any]:
    """
    Builds a search tree from the emoji data for efficient lookup.

    :return: A dictionary representing the search tree.
    """
    global _SEARCH_TREE
    if not _SEARCH_TREE:
        from emojiswahili.unicode_codes import EMOJI_DATA
        for emj, data in EMOJI_DATA.items():
            sub_tree = _SEARCH_TREE
            for char in emj:
                if char not in sub_tree:
                    sub_tree[char] = {}
                sub_tree = sub_tree[char]
            sub_tree['data'] = data
    return _SEARCH_TREE