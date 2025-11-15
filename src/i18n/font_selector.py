"""
Font selection module for bilingual support.

Selects appropriate fonts based on language (Japanese/English).
"""

from typing import Dict


class FontSelector:
    """
    Select appropriate fonts based on language.

    Provides font recommendations for Japanese, English, and mixed content.
    """

    # Japanese fonts (with fallbacks)
    JAPANESE_FONTS = {
        'title': ['Meiryo', 'Yu Gothic', 'MS Gothic', 'DejaVu Sans'],
        'body': ['Meiryo', 'Yu Gothic', 'MS PGothic', 'DejaVu Sans'],
        'heading': ['Meiryo Bold', 'Yu Gothic', 'MS Gothic', 'DejaVu Sans'],
        'monospace': ['MS Gothic', 'Consolas', 'Courier New']
    }

    # English fonts (with fallbacks)
    ENGLISH_FONTS = {
        'title': ['Arial', 'Calibri', 'Helvetica', 'DejaVu Sans'],
        'body': ['Arial', 'Calibri', 'Verdana', 'DejaVu Sans'],
        'heading': ['Arial Black', 'Calibri Bold', 'Helvetica Bold', 'DejaVu Sans'],
        'monospace': ['Consolas', 'Courier New', 'Monaco', 'monospace']
    }

    # Fonts that work well for mixed Japanese/English content
    MIXED_FONTS = {
        'title': ['Meiryo', 'Yu Gothic', 'DejaVu Sans'],
        'body': ['Meiryo', 'Yu Gothic', 'DejaVu Sans'],
        'heading': ['Meiryo Bold', 'Yu Gothic', 'DejaVu Sans'],
        'monospace': ['Consolas', 'Courier New', 'monospace']
    }

    @staticmethod
    def get_font_for_language(
        language: str,
        font_type: str = 'body',
        fallback_index: int = 0
    ) -> str:
        """
        Get appropriate font for language and type.

        Args:
            language: 'ja', 'en', or 'mixed'
            font_type: 'title', 'body', 'heading', or 'monospace'
            fallback_index: Index in fallback list (0 = primary)

        Returns:
            Font name
        """
        if language == 'ja':
            fonts = FontSelector.JAPANESE_FONTS
        elif language == 'en':
            fonts = FontSelector.ENGLISH_FONTS
        else:  # mixed
            fonts = FontSelector.MIXED_FONTS

        font_list = fonts.get(font_type, fonts['body'])

        if fallback_index >= len(font_list):
            fallback_index = len(font_list) - 1

        return font_list[fallback_index]

    @staticmethod
    def get_all_fonts_for_language(language: str) -> Dict[str, str]:
        """
        Get all font types for a language.

        Args:
            language: 'ja', 'en', or 'mixed'

        Returns:
            Dictionary mapping font types to font names
        """
        return {
            'title': FontSelector.get_font_for_language(language, 'title'),
            'body': FontSelector.get_font_for_language(language, 'body'),
            'heading': FontSelector.get_font_for_language(language, 'heading'),
            'monospace': FontSelector.get_font_for_language(language, 'monospace')
        }

    @staticmethod
    def get_mixed_language_fonts() -> Dict[str, str]:
        """
        Get fonts that work for both Japanese and English.

        Returns:
            Dictionary of font types and names
        """
        return {
            'title': 'Meiryo',
            'body': 'Meiryo',
            'heading': 'Meiryo',
            'monospace': 'Consolas'
        }

    @staticmethod
    def get_font_with_fallbacks(language: str, font_type: str = 'body') -> list:
        """
        Get list of fonts with fallbacks.

        Args:
            language: 'ja', 'en', or 'mixed'
            font_type: Type of font

        Returns:
            List of font names in priority order
        """
        if language == 'ja':
            return FontSelector.JAPANESE_FONTS.get(font_type, ['Meiryo'])
        elif language == 'en':
            return FontSelector.ENGLISH_FONTS.get(font_type, ['Arial'])
        else:
            return FontSelector.MIXED_FONTS.get(font_type, ['Meiryo'])

    @staticmethod
    def recommend_font_size(language: str, font_type: str = 'body') -> int:
        """
        Recommend font size based on language.

        Japanese text often needs slightly different sizing than English.

        Args:
            language: 'ja', 'en', or 'mixed'
            font_type: Type of font

        Returns:
            Recommended font size in points
        """
        base_sizes = {
            'title': 44,
            'heading': 28,
            'body': 18,
            'caption': 14,
            'monospace': 14
        }

        base_size = base_sizes.get(font_type, 18)

        # Japanese text can be slightly smaller due to character density
        if language == 'ja' and font_type in ['body', 'caption']:
            return max(12, base_size - 1)

        return base_size
