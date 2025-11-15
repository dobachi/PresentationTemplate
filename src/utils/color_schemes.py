"""
Color scheme management utilities.
"""

from typing import Dict, List


class ColorScheme:
    """
    Color scheme manager for presentations.

    Provides color palettes and helper functions for consistent coloring.
    """

    CORPORATE = {
        'primary': '#0066CC',
        'secondary': '#004C99',
        'accent': '#FF6600',
        'background': '#FFFFFF',
        'text': '#333333',
        'series': ['#0066CC', '#FF6600', '#00CC66', '#CC0066', '#6600CC']
    }

    TECHNICAL = {
        'primary': '#2C3E50',
        'secondary': '#34495E',
        'accent': '#E74C3C',
        'background': '#FFFFFF',
        'text': '#2C3E50',
        'series': ['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6']
    }

    ACADEMIC = {
        'primary': '#003366',
        'secondary': '#0055AA',
        'accent': '#CC9900',
        'background': '#FFFFFF',
        'text': '#000000',
        'series': ['#003366', '#CC9900', '#006633', '#990033', '#663399']
    }

    @staticmethod
    def get_scheme(name: str) -> Dict[str, any]:
        """
        Get color scheme by name.

        Args:
            name: Scheme name ('corporate', 'technical', 'academic')

        Returns:
            Color scheme dictionary
        """
        schemes = {
            'corporate': ColorScheme.CORPORATE,
            'technical': ColorScheme.TECHNICAL,
            'academic': ColorScheme.ACADEMIC
        }

        return schemes.get(name.lower(), ColorScheme.CORPORATE)

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        """
        Convert hex color to RGB tuple.

        Args:
            hex_color: Color in hex format (#RRGGBB)

        Returns:
            Tuple of (R, G, B) values (0-255)
        """
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        """
        Convert RGB to hex color.

        Args:
            r: Red value (0-255)
            g: Green value (0-255)
            b: Blue value (0-255)

        Returns:
            Hex color string (#RRGGBB)
        """
        return f'#{r:02x}{g:02x}{b:02x}'
