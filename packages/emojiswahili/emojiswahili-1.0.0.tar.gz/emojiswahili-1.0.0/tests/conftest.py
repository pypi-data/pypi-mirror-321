import pytest
import functools
import random
import emojiswahili

def pytest_sessionstart():
    """
    Increase cache size to unlimited to avoid cache misses during tests.
    This improves performance for repeated emoji lookups.
    """
    # Just wrap the function itself without .__wrapped__
    emojiswahili.unicode_codes.get_emoji_by_name = functools.lru_cache(maxsize=None)(
        emojiswahili.unicode_codes.get_emoji_by_name
    )

def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--shuffle',
        action='store_true',
        default=False,
        help='Run tests in random order.',
    )

def pytest_collection_modifyitems(config: pytest.Config, items):
    if config.getoption('shuffle'):
        print("\nShuffling tests for a random order")
        random.shuffle(items)