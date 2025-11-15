"""
Statistical chart generation module.

This module provides functionality for creating statistical charts
including line charts, bar charts, scatter plots, and more using
matplotlib and seaborn.
"""

import os
from typing import Dict, List, Any, Optional, Union
import numpy as np


class StatisticalChart:
    """
    Class for creating statistical charts.

    Uses matplotlib and seaborn for generating various chart types.

    Attributes:
        theme: Theme configuration dictionary
        language: Language code for labels
        output_dir: Directory for saving generated charts
    """

    def __init__(
        self,
        theme: Optional[Dict[str, Any]] = None,
        language: str = "ja",
        output_dir: str = "output/charts"
    ):
        """
        Initialize the StatisticalChart generator.

        Args:
            theme: Theme configuration dictionary
            language: Language code ('ja' or 'en')
            output_dir: Output directory for charts
        """
        self.theme = theme or self._get_default_theme()
        self.language = language
        self.output_dir = output_dir

        os.makedirs(output_dir, exist_ok=True)
        self._configure_matplotlib()

    def _get_default_theme(self) -> Dict[str, Any]:
        """Get default theme configuration."""
        return {
            'colors': {
                'primary': '#0066CC',
                'secondary': '#004C99',
                'accent': '#FF6600',
                'series': ['#0066CC', '#FF6600', '#00CC66', '#CC0066', '#6600CC']
            }
        }

    def _configure_matplotlib(self):
        """Configure matplotlib settings for charts."""
        try:
            import matplotlib.pyplot as plt
            import seaborn as sns

            # Set style
            sns.set_style("whitegrid")

            # Configure fonts
            if self.language == 'ja':
                plt.rcParams['font.sans-serif'] = ['Meiryo', 'Hiragino Sans', 'Yu Gothic', 'DejaVu Sans']
            else:
                plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

            plt.rcParams['font.family'] = 'sans-serif'
            plt.rcParams['axes.unicode_minus'] = False

            # Set default figure size
            plt.rcParams['figure.figsize'] = (10, 6)

        except Exception as e:
            print(f"Warning: Could not configure matplotlib: {e}")

    def _get_colors(self, n: int) -> List[str]:
        """
        Get n colors from theme.

        Args:
            n: Number of colors needed

        Returns:
            List of color hex strings
        """
        series_colors = self.theme['colors'].get('series', ['#0066CC'])
        colors = []

        for i in range(n):
            colors.append(series_colors[i % len(series_colors)])

        return colors

    def create_line_chart(
        self,
        data: Dict[str, List[Union[int, float]]],
        labels: Dict[str, str],
        title: str = "",
        filename: str = "line_chart"
    ) -> str:
        """
        Create a line chart.

        Args:
            data: Dictionary with 'x' and one or more 'y' series
                  e.g., {'x': [...], 'y1': [...], 'y2': [...]}
            labels: Dictionary with axis labels and legend
                    e.g., {'x_axis': 'Year', 'y_axis': 'Value', 'y1': 'Series 1'}
            title: Chart title
            filename: Output filename

        Returns:
            Path to generated chart
        """
        try:
            import matplotlib.pyplot as plt

            output_path = os.path.join(self.output_dir, filename + ".png")

            fig, ax = plt.subplots(figsize=(10, 6))

            x_data = data.get('x', [])
            y_keys = [k for k in data.keys() if k.startswith('y')]

            colors = self._get_colors(len(y_keys))

            for i, y_key in enumerate(y_keys):
                y_data = data.get(y_key, [])
                label = labels.get(y_key, y_key)

                ax.plot(
                    x_data, y_data,
                    marker='o',
                    linewidth=2,
                    markersize=8,
                    color=colors[i],
                    label=label
                )

            ax.set_xlabel(labels.get('x_axis', 'X'), fontsize=12)
            ax.set_ylabel(labels.get('y_axis', 'Y'), fontsize=12)

            if title:
                ax.set_title(title, fontsize=14, fontweight='bold')

            if len(y_keys) > 1:
                ax.legend()

            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()

            return output_path

        except ImportError as e:
            print(f"Error: matplotlib not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating line chart: {e}")
            return ""

    def create_bar_chart(
        self,
        data: Dict[str, List[Union[int, float]]],
        labels: Dict[str, str],
        title: str = "",
        orientation: str = 'vertical',
        filename: str = "bar_chart"
    ) -> str:
        """
        Create a bar chart.

        Args:
            data: Dictionary with 'categories' and value series
            labels: Dictionary with axis labels
            title: Chart title
            orientation: 'vertical' or 'horizontal'
            filename: Output filename

        Returns:
            Path to generated chart
        """
        try:
            import matplotlib.pyplot as plt
            import numpy as np

            output_path = os.path.join(self.output_dir, filename + ".png")

            fig, ax = plt.subplots(figsize=(10, 6))

            categories = data.get('categories', [])
            value_keys = [k for k in data.keys() if k.startswith('values')]

            if not value_keys:
                # Single series
                values = data.get('values', [])

                if orientation == 'horizontal':
                    ax.barh(categories, values, color=self.theme['colors']['primary'])
                    ax.set_xlabel(labels.get('value_axis', 'Value'), fontsize=12)
                    ax.set_ylabel(labels.get('category_axis', 'Category'), fontsize=12)
                else:
                    ax.bar(categories, values, color=self.theme['colors']['primary'])
                    ax.set_xlabel(labels.get('category_axis', 'Category'), fontsize=12)
                    ax.set_ylabel(labels.get('value_axis', 'Value'), fontsize=12)

            else:
                # Multiple series (grouped bar chart)
                x = np.arange(len(categories))
                width = 0.8 / len(value_keys)
                colors = self._get_colors(len(value_keys))

                for i, value_key in enumerate(value_keys):
                    values = data.get(value_key, [])
                    offset = (i - len(value_keys)/2) * width + width/2
                    label = labels.get(value_key, value_key)

                    if orientation == 'horizontal':
                        ax.barh(x + offset, values, width, label=label, color=colors[i])
                    else:
                        ax.bar(x + offset, values, width, label=label, color=colors[i])

                if orientation == 'horizontal':
                    ax.set_yticks(x)
                    ax.set_yticklabels(categories)
                    ax.set_xlabel(labels.get('value_axis', 'Value'), fontsize=12)
                    ax.set_ylabel(labels.get('category_axis', 'Category'), fontsize=12)
                else:
                    ax.set_xticks(x)
                    ax.set_xticklabels(categories, rotation=45, ha='right')
                    ax.set_xlabel(labels.get('category_axis', 'Category'), fontsize=12)
                    ax.set_ylabel(labels.get('value_axis', 'Value'), fontsize=12)

                ax.legend()

            if title:
                ax.set_title(title, fontsize=14, fontweight='bold')

            ax.grid(True, alpha=0.3, axis='y' if orientation == 'vertical' else 'x')
            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()

            return output_path

        except ImportError as e:
            print(f"Error: Required library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating bar chart: {e}")
            return ""

    def create_scatter_plot(
        self,
        data: Dict[str, List[Union[int, float]]],
        labels: Dict[str, str],
        title: str = "",
        filename: str = "scatter_plot"
    ) -> str:
        """
        Create a scatter plot.

        Args:
            data: Dictionary with 'x' and 'y' data, optionally 'size' and 'color'
            labels: Dictionary with axis labels
            title: Chart title
            filename: Output filename

        Returns:
            Path to generated chart
        """
        try:
            import matplotlib.pyplot as plt

            output_path = os.path.join(self.output_dir, filename + ".png")

            fig, ax = plt.subplots(figsize=(10, 6))

            x_data = data.get('x', [])
            y_data = data.get('y', [])
            sizes = data.get('size', [100] * len(x_data))
            colors_data = data.get('color', [self.theme['colors']['primary']] * len(x_data))

            ax.scatter(
                x_data, y_data,
                s=sizes,
                c=colors_data,
                alpha=0.6,
                edgecolors='black',
                linewidth=1
            )

            ax.set_xlabel(labels.get('x_axis', 'X'), fontsize=12)
            ax.set_ylabel(labels.get('y_axis', 'Y'), fontsize=12)

            if title:
                ax.set_title(title, fontsize=14, fontweight='bold')

            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()

            return output_path

        except ImportError as e:
            print(f"Error: matplotlib not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating scatter plot: {e}")
            return ""

    def create_pie_chart(
        self,
        data: Dict[str, Union[List[str], List[float]]],
        title: str = "",
        filename: str = "pie_chart"
    ) -> str:
        """
        Create a pie chart.

        Args:
            data: Dictionary with 'labels' and 'values'
            title: Chart title
            filename: Output filename

        Returns:
            Path to generated chart
        """
        try:
            import matplotlib.pyplot as plt

            output_path = os.path.join(self.output_dir, filename + ".png")

            fig, ax = plt.subplots(figsize=(8, 8))

            labels = data.get('labels', [])
            values = data.get('values', [])
            colors = self._get_colors(len(labels))

            ax.pie(
                values,
                labels=labels,
                colors=colors,
                autopct='%1.1f%%',
                startangle=90,
                textprops={'fontsize': 11}
            )

            ax.axis('equal')

            if title:
                ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()

            return output_path

        except ImportError as e:
            print(f"Error: matplotlib not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating pie chart: {e}")
            return ""
