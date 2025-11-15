"""
Comparison chart generation module.

Provides specialized charts for comparing data across categories.
"""

import os
from typing import Dict, List, Any, Optional, Union


class ComparisonChart:
    """
    Class for creating comparison charts.

    Supports radar charts, stacked bar charts, and grouped comparisons.
    """

    def __init__(
        self,
        theme: Optional[Dict[str, Any]] = None,
        language: str = "ja",
        output_dir: str = "output/charts"
    ):
        """
        Initialize the ComparisonChart generator.

        Args:
            theme: Theme configuration dictionary
            language: Language code ('ja' or 'en')
            output_dir: Output directory for charts
        """
        self.theme = theme or {}
        self.language = language
        self.output_dir = output_dir

        os.makedirs(output_dir, exist_ok=True)

    def create_stacked_bar_chart(
        self,
        data: Dict[str, Any],
        labels: Dict[str, str],
        title: str = "",
        filename: str = "stacked_bar"
    ) -> str:
        """Create a stacked bar chart."""
        try:
            import matplotlib.pyplot as plt
            import numpy as np

            output_path = os.path.join(self.output_dir, filename + ".png")

            fig, ax = plt.subplots(figsize=(10, 6))

            categories = data.get('categories', [])
            series = {k: v for k, v in data.items() if k.startswith('series')}

            bottoms = np.zeros(len(categories))

            for i, (key, values) in enumerate(series.items()):
                label = labels.get(key, key)
                ax.bar(categories, values, bottom=bottoms, label=label)
                bottoms += np.array(values)

            ax.set_xlabel(labels.get('x_axis', 'Category'), fontsize=12)
            ax.set_ylabel(labels.get('y_axis', 'Value'), fontsize=12)

            if title:
                ax.set_title(title, fontsize=14, fontweight='bold')

            ax.legend()
            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            return output_path

        except Exception as e:
            print(f"Error creating stacked bar chart: {e}")
            return ""
