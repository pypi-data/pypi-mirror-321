"""
Testing utilities for emoji handling and Swahili translations.
"""

from typing import Generator, Dict, Any, Tuple, Iterable
import unicodedata
import pytest

import emojiswahili.unicode_codes

_NormalizationForm = Literal['NFC', 'NFD', 'NFKC', 'NFKD']


@pytest.fixture
def load_swahili_language():
    """Load the Swahili language pack into EMOJI_DATA."""
    emojiswahili.config.load_language('sw')
    yield


def ascii(s: str) -> str:
    """
    Return escaped Unicode code points for non-ASCII characters.
    Example: "😊" -> "\\U0001f60a"
    """
    return s.encode('unicode-escape').decode()


def normalize(form: _NormalizationForm, s: str) -> str:
    """
    Normalize a string to the specified Unicode normalization form.
    """
    return unicodedata.normalize(form, s)


def is_normalized(form: _NormalizationForm, s: str) -> bool:
    """
    Check if a string is in the specified Unicode normalization form.
    """
    return unicodedata.is_normalized(form, s) if hasattr(unicodedata, "is_normalized") else normalize(form, s) == s


def get_swahili_emoji_dict() -> Dict[str, Any]:
    """
    Generate a dictionary containing all Swahili translations for fully qualified emoji.
    The dictionary is cached in _EMOJI_UNICODE['sw'] after the first generation.
    """
    emojiswahili.config.load_language('sw')
    return {
        data['sw']: emj
        for emj, data in emojiswahili.EMOJI_DATA.items()
        if 'sw' in data and data['status'] <= emojiswahili.STATUS['fully_qualified']
    }


def all_swahili_emoji() -> Generator[Tuple[str, str], None, None]:
    """
    Yield all Swahili-translated emoji and their respective Unicode values.
    """
    swahili_dict = get_swahili_emoji_dict()
    for name, emj in swahili_dict.items():
        yield (name, emj)