from emojiswahili.unicode_codes.data_dict import LANGUAGES

class Config:
    def __init__(self):
        self.loaded_languages = set()

    def load_language(self, lang: str):
        """
        Load language data for the specified language.

        :param lang: Language code to load (e.g., 'sw').
        """
        if lang not in LANGUAGES:
            raise ValueError(f"Language '{lang}' is not available.")
        self.loaded_languages.add(lang)
        print(f"Language '{lang}' loaded successfully.")

# Create a global config object
config = Config()