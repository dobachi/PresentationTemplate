"""
Language detection module.

Detects whether text is Japanese, English, or mixed.
"""

import re
from typing import List, Dict


class LanguageDetector:
    """
    Detect language from text or conversation.

    Supports Japanese, English, and mixed language detection.
    """

    # Japanese character ranges
    HIRAGANA = re.compile(r'[\u3040-\u309F]')
    KATAKANA = re.compile(r'[\u30A0-\u30FF]')
    KANJI = re.compile(r'[\u4E00-\u9FFF]')
    JAPANESE = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]')

    # English characters
    LATIN = re.compile(r'[a-zA-Z]')

    @staticmethod
    def detect_from_text(text: str) -> str:
        """
        Detect if text is Japanese, English, or mixed.

        Args:
            text: Text to analyze

        Returns:
            'ja', 'en', or 'mixed'
        """
        if not text:
            return 'en'  # Default to English

        # Count Japanese and Latin characters
        japanese_chars = len(LanguageDetector.JAPANESE.findall(text))
        latin_chars = len(LanguageDetector.LATIN.findall(text))

        total_chars = japanese_chars + latin_chars

        if total_chars == 0:
            return 'en'

        japanese_ratio = japanese_chars / total_chars
        latin_ratio = latin_chars / total_chars

        # Determine language based on character ratios
        if japanese_ratio > 0.3:
            if latin_ratio > 0.2:
                return 'mixed'
            return 'ja'
        else:
            return 'en'

    @staticmethod
    def detect_from_conversation(messages: List[str]) -> str:
        """
        Analyze conversation history to determine primary language.

        Args:
            messages: List of conversation messages

        Returns:
            'ja', 'en', or 'mixed'
        """
        if not messages:
            return 'en'

        # Combine all messages
        combined_text = ' '.join(messages)

        return LanguageDetector.detect_from_text(combined_text)

    @staticmethod
    def has_japanese(text: str) -> bool:
        """
        Check if text contains any Japanese characters.

        Args:
            text: Text to check

        Returns:
            True if Japanese characters found
        """
        return bool(LanguageDetector.JAPANESE.search(text))

    @staticmethod
    def is_mostly_japanese(text: str, threshold: float = 0.5) -> bool:
        """
        Check if text is mostly Japanese.

        Args:
            text: Text to analyze
            threshold: Minimum ratio of Japanese chars (0.0-1.0)

        Returns:
            True if Japanese ratio exceeds threshold
        """
        if not text:
            return False

        japanese_chars = len(LanguageDetector.JAPANESE.findall(text))
        total_chars = len(text.replace(' ', '').replace('\n', ''))

        if total_chars == 0:
            return False

        return (japanese_chars / total_chars) >= threshold

    @staticmethod
    def get_language_stats(text: str) -> Dict[str, any]:
        """
        Get detailed language statistics.

        Args:
            text: Text to analyze

        Returns:
            Dictionary with character counts and ratios
        """
        hiragana_count = len(LanguageDetector.HIRAGANA.findall(text))
        katakana_count = len(LanguageDetector.KATAKANA.findall(text))
        kanji_count = len(LanguageDetector.KANJI.findall(text))
        latin_count = len(LanguageDetector.LATIN.findall(text))

        total_chars = hiragana_count + katakana_count + kanji_count + latin_count

        return {
            'hiragana': hiragana_count,
            'katakana': katakana_count,
            'kanji': kanji_count,
            'japanese_total': hiragana_count + katakana_count + kanji_count,
            'latin': latin_count,
            'total_chars': total_chars,
            'japanese_ratio': (hiragana_count + katakana_count + kanji_count) / total_chars if total_chars > 0 else 0,
            'latin_ratio': latin_count / total_chars if total_chars > 0 else 0,
            'detected_language': LanguageDetector.detect_from_text(text)
        }
