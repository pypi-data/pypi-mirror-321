"""
emoji.core
~~~~~~~~~~

Core components for Swahili emoji support.
"""

import re
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Union
from emojiswahili.unicode_codes import EMOJI_DATA, get_emoji_by_name

__all__ = [
    'emojize',
    'demojize',
    'emoji_list',
    'distinct_emoji_list',
    'emoji_count',
    'is_emoji',
    'purely_emoji',
]

_DEFAULT_DELIMITER = ':'

def emojize(
    string: str,
    delimiters: Tuple[str, str] = (_DEFAULT_DELIMITER, _DEFAULT_DELIMITER),
) -> str:
    """
    Replace Swahili emoji names in a string with Unicode codes.
    Example:
        >>> emojize("Mshindi wakwanza anapata :nishani_ya_dhababu:")
        Mshindi wakwanza anapata 🥇

    :param string: String containing Swahili emoji names.
    :param delimiters: (optional) Delimiters for emoji names (default is ':').
    """
    pattern = re.compile(
        f'{re.escape(delimiters[0])}([^ {re.escape(delimiters[1])}]+){re.escape(delimiters[1])}'
    )

    def replace(match):
        name = f'{delimiters[0]}{match.group(1)}{delimiters[1]}'
        emj = get_emoji_by_name(name)
        return emj if emj else match.group(0)

    return pattern.sub(replace, string)


def demojize(
    string: str,
    delimiters: Tuple[str, str] = (':', ':')
) -> str:
    def replace(emj):
        if emj in EMOJI_DATA:
            code = EMOJI_DATA[emj]['sw']
            # If code is already wrapped in colons, strip them
            if code.startswith(delimiters[0]) and code.endswith(delimiters[1]):
                code = code[len(delimiters[0]):-len(delimiters[1])]
            return f"{delimiters[0]}{code}{delimiters[1]}"
        return emj

    return ''.join(
        replace(char) if is_emoji(char) else char
        for char in string
    )



def emoji_list(string: str) -> List[Dict[str, Any]]:
    """
    Returns a list of emoji in the string with their locations.
    Example:
        >>> emoji_list("Hii ni 🥇 na 🥈")
        [{'match_start': 7, 'match_end': 8, 'emoji': '🥇'},
         {'match_start': 12, 'match_end': 13, 'emoji': '🥈'}]
    """
    return [
        {'match_start': idx, 'match_end': idx + 1, 'emoji': char}
        for idx, char in enumerate(string)
        if is_emoji(char)
    ]


def distinct_emoji_list(string: str) -> List[str]:
    """Returns a list of distinct emojis in the string."""
    return list(set(char for char in string if is_emoji(char)))


def emoji_count(string: str, unique: bool = False) -> int:
    """Counts emojis in the string. Set unique=True for distinct count."""
    return len(distinct_emoji_list(string)) if unique else sum(is_emoji(char) for char in string)


def is_emoji(string: str) -> bool:
    """Returns True if the character is a valid Unicode emoji."""
    return string in EMOJI_DATA


def purely_emoji(string: str) -> bool:
    """Returns True if the string consists only of emojis."""
    return all(is_emoji(char) for char in string)