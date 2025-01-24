import emojiswahili

def test_emoji_data_loaded():
    """
    Simple check to confirm EMOJI_DATA is loaded from emoji.json
    and that some known emojis exist.
    """
    data = emojiswahili.EMOJI_DATA
    assert isinstance(data, dict)
    # Check a few known emojis exist
    assert "🥇" in data, "🥇 (Gold Medal) should be in the emoji data"
    assert "🥈" in data, "🥈 (Silver Medal) should be in the emoji data"
    assert "🥉" in data, "🥉 (Bronze Medal) should be in the emoji data"

def test_swahili_translation():
    """
    Confirm a few known emojis have the correct Swahili shortcodes.
    """
    data = emojiswahili.EMOJI_DATA
    # Assuming your code wraps shortcodes under the 'sw' key
    assert data["🥇"]["sw"] == ":nishani_ya_dhababu:"
    assert data["🥈"]["sw"] == ":nishani_ya_fedha:"
    assert data["🥉"]["sw"] == ":nishani_ya_shaba:"
