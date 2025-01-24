__all__ = ['LANGUAGES', 'STATUS']

from typing import Any, Dict

component = 1
fully_qualified = 2
minimally_qualified = 3
unqualified = 4

STATUS: Dict[str, int] = {
    'component': component,
    'fully_qualified': fully_qualified,
    'minimally_qualified': minimally_qualified,
    'unqualified': unqualified,
}

LANGUAGES: Dict[str, str] = {
    'sw': 'Swahili',
}