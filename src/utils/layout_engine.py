"""
Layout engine for smart positioning of elements on slides.
"""

from typing import Dict, List, Tuple
from pptx.util import Inches


class LayoutEngine:
    """
    Smart layout engine for positioning elements on slides.

    Handles automatic centering, sizing, and positioning of diagrams,
    charts, and text elements.
    """

    # Standard slide dimensions (in inches)
    SLIDE_WIDTH = 10
    SLIDE_HEIGHT = 7.5

    # Standard margins (in inches)
    MARGIN_LEFT = 0.5
    MARGIN_RIGHT = 0.5
    MARGIN_TOP = 0.5
    MARGIN_BOTTOM = 0.5

    # Title area
    TITLE_HEIGHT = 1.0

    @staticmethod
    def calculate_content_area() -> Dict[str, float]:
        """
        Calculate the usable content area.

        Returns:
            Dictionary with left, top, width, height in inches
        """
        return {
            'left': LayoutEngine.MARGIN_LEFT,
            'top': LayoutEngine.MARGIN_TOP + LayoutEngine.TITLE_HEIGHT,
            'width': LayoutEngine.SLIDE_WIDTH - LayoutEngine.MARGIN_LEFT - LayoutEngine.MARGIN_RIGHT,
            'height': LayoutEngine.SLIDE_HEIGHT - LayoutEngine.MARGIN_TOP - LayoutEngine.MARGIN_BOTTOM - LayoutEngine.TITLE_HEIGHT
        }

    @staticmethod
    def center_image(
        image_width: float,
        image_height: float,
        respect_aspect: bool = True
    ) -> Tuple[float, float, float, float]:
        """
        Calculate position and size to center an image.

        Args:
            image_width: Original image width
            image_height: Original image height
            respect_aspect: Whether to maintain aspect ratio

        Returns:
            Tuple of (left, top, width, height) in inches
        """
        content = LayoutEngine.calculate_content_area()

        if respect_aspect:
            # Calculate scale to fit in content area
            scale_w = content['width'] / image_width if image_width > 0 else 1
            scale_h = content['height'] / image_height if image_height > 0 else 1
            scale = min(scale_w, scale_h, 1.0)  # Don't upscale

            new_width = image_width * scale
            new_height = image_height * scale
        else:
            new_width = content['width']
            new_height = content['height']

        # Center in content area
        left = content['left'] + (content['width'] - new_width) / 2
        top = content['top'] + (content['height'] - new_height) / 2

        return (left, top, new_width, new_height)

    @staticmethod
    def two_column_layout() -> List[Dict[str, float]]:
        """
        Calculate positions for two-column layout.

        Returns:
            List of two dictionaries with column specifications
        """
        content = LayoutEngine.calculate_content_area()

        column_gap = 0.5
        column_width = (content['width'] - column_gap) / 2

        return [
            {
                'left': content['left'],
                'top': content['top'],
                'width': column_width,
                'height': content['height']
            },
            {
                'left': content['left'] + column_width + column_gap,
                'top': content['top'],
                'width': column_width,
                'height': content['height']
            }
        ]

    @staticmethod
    def grid_layout(rows: int, cols: int) -> List[List[Dict[str, float]]]:
        """
        Calculate positions for grid layout.

        Args:
            rows: Number of rows
            cols: Number of columns

        Returns:
            2D list of cell specifications
        """
        content = LayoutEngine.calculate_content_area()

        gap = 0.3
        cell_width = (content['width'] - gap * (cols - 1)) / cols
        cell_height = (content['height'] - gap * (rows - 1)) / rows

        grid = []
        for row in range(rows):
            row_cells = []
            for col in range(cols):
                row_cells.append({
                    'left': content['left'] + col * (cell_width + gap),
                    'top': content['top'] + row * (cell_height + gap),
                    'width': cell_width,
                    'height': cell_height
                })
            grid.append(row_cells)

        return grid

    @staticmethod
    def inches_to_emu(inches: float) -> int:
        """
        Convert inches to EMU (English Metric Units).

        Args:
            inches: Value in inches

        Returns:
            Value in EMU
        """
        return int(inches * 914400)

    @staticmethod
    def emu_to_inches(emu: int) -> float:
        """
        Convert EMU to inches.

        Args:
            emu: Value in EMU

        Returns:
            Value in inches
        """
        return emu / 914400
