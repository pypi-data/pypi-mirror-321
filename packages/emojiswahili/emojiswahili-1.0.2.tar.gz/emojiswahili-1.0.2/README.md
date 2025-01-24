# emojiswahili

**Emojiswahili** is a Python library for working with emojis in Swahili.
---

## Features

- **Supports Swahili translations** for Unicode emojis.
- **Converts text with Swahili emoji codes** (e.g., `:nishani_ya_dhababu:`) **to Unicode emojis** (e.g., `🥇`).
- **Converts Unicode emojis** back **to Swahili emoji codes**.
- **Lists all emojis in a string** (with their positions), e.g., `emoji_list()`.
- **Extracts distinct emojis** in a string, e.g., `distinct_emoji_list()`.
- **Counts emojis** in a string (optionally only unique ones), e.g., `emoji_count()`.
- **Checks if a string is purely emoji**, e.g., `purely_emoji()`.

---


## Example Usage

Emojis defined by the [`Unicode consortium`](https://unicode.org/emoji/charts/full-emoji-list.html)  
can be easily used with Swahili translations.

```python 
>>> import emojiswahili

# Emojize a string
>>> print(emojiswahili.emojize('Mshindi wakwanza anapata :nishani_ya_dhababu:'))
Mshindi wakwanza anapata 🥇

# Demojize a string
>>> print(emojiswahili.demojize('Mshindi wakwanza anapata 🥇'))
Mshindi wakwanza anapata :nishani_ya_dhababu:

# List all emojis (with positions) in a string
>>> text = "Hii ni 🥇 na 🥈"
>>> emoji_positions = emojiswahili.emoji_list(text)
>>> print(emoji_positions)
[{'match_start': 7, 'match_end': 8, 'emoji': '🥇'},
 {'match_start': 12, 'match_end': 13, 'emoji': '🥈'}]

# Get a list of distinct emojis
>>> print(emojiswahili.distinct_emoji_list(text))
['🥇', '🥈']

# Count emojis in a string
>>> print(emojiswahili.emoji_count(text))
2
>>> print(emojiswahili.emoji_count(text, unique=True))
2

# Check if a string is purely emoji
>>> print(emojiswahili.purely_emoji('🥇🥈'))
True
>>> print(emojiswahili.purely_emoji('Hii ni 🥇 na 🥈'))
False

```

---

## Installation

Install via pip:

```console
$ python -m pip install emojiswahili --upgrade
```

---

## Development Guide

### Code Style Check

Ensure the code adheres to style guidelines using `ruff`:

```console
$ python -m pip install ruff
$ ruff check emojiswahili
```

### Type Checking

Test the type hints using `pyright` or `mypy`:

```console
$ python -m pip install pyright mypy typeguard
$ pyright emojiswahili
$ pyright tests
$ mypy emojiswahili
$ pytest --typeguard-packages=emojiswahili
```

---

## Emoji Lists

### Swahili Emoji List

You can find the complete Swahili emoji list at:

- [`Unicode Emoji List in Swahili`](https://emojiterra.com/keyboard/sw)  

---

## Authors and Maintainers

This project is developed and maintained by the eGARIDC Team / [`@ega`](https://ega.go.tz/)
