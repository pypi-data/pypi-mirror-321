import pytest
import emojiswahili


def test_emojize():
    """
    Test converting Swahili shortcodes to actual emojis.
    """
    # Single emoji
    assert emojiswahili.emojize(":nishani_ya_dhababu:") == "🥇"

    # Mixed text
    text = "Hii ni medali :nishani_ya_fedha:!"
    assert emojiswahili.emojize(text) == "Hii ni medali 🥈!"

    # Unknown shortcode remains unchanged
    assert emojiswahili.emojize(":shortcode_isiyo_julikana:") == ":shortcode_isiyo_julikana:"


def test_demojize():
    """
    Test converting emojis back to Swahili shortcodes.
    """
    # Single emoji
    assert emojiswahili.demojize("🥇") == ":nishani_ya_dhababu:"

    # Mixed text
    text = "Mshindi wakwanza anapata 🥉"
    assert emojiswahili.demojize(text) == "Mshindi wakwanza anapata :nishani_ya_shaba:"

    # Non-emoji remains unchanged
    assert emojiswahili.demojize("Hello!") == "Hello!"


def test_emoji_list():
    """
    Test extracting a list of emojis with positions.
    """
    text = "Python 🥇 is awesome 🥈!"
    result = emojiswahili.emoji_list(text)
    # Example result: [
    #   {'match_start': 7, 'match_end': 8, 'emoji': '🥇'},
    #   {'match_start': 20, 'match_end': 21, 'emoji': '🥈'}
    # ]
    assert len(result) == 2
    assert result[0]['emoji'] == '🥇'
    assert result[1]['emoji'] == '🥈'


def test_distinct_emoji_list():
    """
    Test extracting a distinct list of emojis.
    """
    text = "🥇🥈🥇"
    result = emojiswahili.distinct_emoji_list(text)
    # Should only have 🥇 and 🥈 once each
    assert len(result) == 2
    assert sorted(result) == sorted(["🥇", "🥈"])


def test_emoji_count():
    """
    Test counting total emojis vs. counting unique emojis.
    """
    text = "Hii ni 🥇 na 🥇 nyingine"
    assert emojiswahili.emoji_count(text) == 2
    assert emojiswahili.emoji_count(text, unique=True) == 1


def test_is_emoji():
    """
    Test checking if a single character is an emoji.
    """
    assert emojiswahili.is_emoji("🥇") is True
    assert emojiswahili.is_emoji("A") is False
    assert emojiswahili.is_emoji("🏧") is True


def test_purely_emoji():
    """
    Test checking if the entire string is made of emojis.
    """
    assert emojiswahili.purely_emoji("🥇🥈🥉") is True
    assert emojiswahili.purely_emoji("🥇🥈Medali") is False
    assert emojiswahili.purely_emoji("") is True  # Edge case: empty string has no non-emoji
