import json
from pathlib import Path
from typing import Dict, Any, Optional
from .data_dict import LANGUAGES, STATUS

__all__ = [
    'get_emoji_by_name',
    'EMOJI_DATA',
    'LANGUAGES',
    'STATUS',
]

# Emoji data
EMOJI_DATA: Dict[str, Dict[str, Any]] = {}

# Load Swahili emoji data during initialization
def _load_default_from_json():
    global EMOJI_DATA
    file = Path(__file__).with_name('emoji.json')
    with open(file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        # Wrap each shortcode under the 'sw' key
        EMOJI_DATA.update({emoji: {'sw': code} for emoji, code in raw_data.items()})

_load_default_from_json()

def get_emoji_by_name(name: str) -> Optional[str]:
    """
    Find emoji by short-name in Swahili.
    Returns None if not found.

    :param name: Emoji short code e.g. ":nishani_ya_dhababu:"
    """
    for emoji, data in EMOJI_DATA.items():
        if data.get('sw') == name:
            return emoji
    return None