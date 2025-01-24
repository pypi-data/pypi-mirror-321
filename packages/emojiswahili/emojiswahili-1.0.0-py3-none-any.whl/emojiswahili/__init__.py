__all__ = [
    # Core functions
    'emojize',
    'demojize',
    'emoji_list',
    'distinct_emoji_list',
    'emoji_count',
    'is_emoji',
    'purely_emoji',
    'version',

    # Unicode codes
    'EMOJI_DATA',
    'LANGUAGES',
    'STATUS',

    # Configuration
    'config',
]

__version__ = '1.0.0'
__author__ = 'eGARIDC'
__email__ = 'info@ega.go.tz'
__license__ = """
New BSD License

Copyright (c) 2025, eGARIDC
All rights reserved.

... [License Text Continues]
"""

from emojiswahili.core import (
    emojize,
    demojize,
    emoji_list,
    distinct_emoji_list,
    emoji_count,
    is_emoji,
    purely_emoji,
)
from emojiswahili.unicode_codes import (
    EMOJI_DATA,
    LANGUAGES,
    STATUS,
    get_emoji_by_name,
)
from emojiswahili.config import config