"""
Layout adjustment module for different languages.

Adjusts text box sizes, line spacing, and layout based on language.
"""

from typing import Tuple


class LayoutAdjuster:
    """
    Adjust layouts for different languages.

    Japanese and English have different text characteristics,
    requiring different layout adjustments.
    """

    # Line spacing multipliers
    LINE_SPACING = {
        'ja': 0.9,   # Tighter for Japanese
        'en': 1.0,   # Standard for English
        'mixed': 0.95  # Compromise for mixed
    }

    # Character width estimates (relative)
    CHAR_WIDTH_RATIO = {
        'ja': 1.2,   # Japanese chars are wider
        'en': 1.0,   # English baseline
        'mixed': 1.1  # Average for mixed
    }

    @staticmethod
    def get_line_spacing(language: str) -> float:
        """
        Get recommended line spacing for language.

        Args:
            language: 'ja', 'en', or 'mixed'

        Returns:
            Line spacing multiplier
        """
        return LayoutAdjuster.LINE_SPACING.get(language, 1.0)

    @staticmethod
    def estimate_text_width(
        text: str,
        language: str,
        font_size: int = 18
    ) -> float:
        """
        Estimate text width in inches.

        Args:
            text: Text to measure
            language: Language code
            font_size: Font size in points

        Returns:
            Estimated width in inches
        """
        char_count = len(text)

        # Base character width in inches (approximate for 18pt font)
        base_char_width = 0.12  # inches per character

        # Adjust for font size
        size_factor = font_size / 18

        # Adjust for language
        lang_factor = LayoutAdjuster.CHAR_WIDTH_RATIO.get(language, 1.0)

        return char_count * base_char_width * size_factor * lang_factor

    @staticmethod
    def estimate_text_height(
        text: str,
        box_width: float,
        language: str,
        font_size: int = 18
    ) -> float:
        """
        Estimate text height based on wrapping.

        Args:
            text: Text to measure
            box_width: Width of text box in inches
            language: Language code
            font_size: Font size in points

        Returns:
            Estimated height in inches
        """
        text_width = LayoutAdjuster.estimate_text_width(text, language, font_size)

        # Calculate number of lines needed
        lines = max(1, int(text_width / box_width) + 1)

        # Line height in inches (approximate)
        line_height = (font_size / 72) * LayoutAdjuster.get_line_spacing(language)

        return lines * line_height

    @staticmethod
    def adjust_text_box_size(
        text: str,
        language: str,
        max_width: float = 8.0,
        font_size: int = 18
    ) -> Tuple[float, float]:
        """
        Calculate optimal text box size for text.

        Args:
            text: Text content
            language: Language code
            max_width: Maximum width in inches
            font_size: Font size in points

        Returns:
            Tuple of (width, height) in inches
        """
        text_width = LayoutAdjuster.estimate_text_width(text, language, font_size)

        # Width: don't exceed max_width
        width = min(text_width + 0.5, max_width)  # Add padding

        # Height: calculate based on wrapping
        height = LayoutAdjuster.estimate_text_height(text, width, language, font_size)

        # Add vertical padding
        height += 0.3

        return (width, height)

    @staticmethod
    def calculate_optimal_font_size(
        text: str,
        box_width: float,
        box_height: float,
        language: str,
        min_size: int = 12,
        max_size: int = 28
    ) -> int:
        """
        Calculate optimal font size to fit text in box.

        Args:
            text: Text to fit
            box_width: Box width in inches
            box_height: Box height in inches
            language: Language code
            min_size: Minimum font size
            max_size: Maximum font size

        Returns:
            Recommended font size in points
        """
        # Try font sizes from max to min
        for size in range(max_size, min_size - 1, -1):
            estimated_height = LayoutAdjuster.estimate_text_height(
                text, box_width, language, size
            )

            if estimated_height <= box_height:
                return size

        return min_size

    @staticmethod
    def adjust_bullet_indent(language: str) -> float:
        """
        Get bullet point indentation for language.

        Args:
            language: Language code

        Returns:
            Indent width in inches
        """
        # Japanese: slightly less indent due to wider characters
        if language == 'ja':
            return 0.3
        else:
            return 0.4

    @staticmethod
    def get_paragraph_spacing(language: str) -> float:
        """
        Get paragraph spacing for language.

        Args:
            language: Language code

        Returns:
            Spacing in points
        """
        if language == 'ja':
            return 6  # Tighter spacing
        else:
            return 8  # Standard spacing
