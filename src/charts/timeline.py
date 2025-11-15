"""
Timeline chart generation module.

Provides timeline and roadmap visualizations.
"""

import os
from typing import Dict, List, Any, Optional


class TimelineChart:
    """
    Class for creating timeline charts.

    Supports Gantt charts, milestones, and roadmaps.
    """

    def __init__(
        self,
        theme: Optional[Dict[str, Any]] = None,
        language: str = "ja",
        output_dir: str = "output/charts"
    ):
        """Initialize the TimelineChart generator."""
        self.theme = theme or {}
        self.language = language
        self.output_dir = output_dir

        os.makedirs(output_dir, exist_ok=True)

    def create_milestone_timeline(
        self,
        milestones: List[Dict[str, Any]],
        title: str = "",
        filename: str = "timeline"
    ) -> str:
        """
        Create a milestone timeline.

        Args:
            milestones: List of milestones with 'date', 'label'
            title: Chart title
            filename: Output filename

        Returns:
            Path to generated chart
        """
        try:
            import matplotlib.pyplot as plt
            import matplotlib.dates as mdates
            from datetime import datetime

            output_path = os.path.join(self.output_dir, filename + ".png")

            fig, ax = plt.subplots(figsize=(12, 4))

            dates = [datetime.strptime(m['date'], '%Y-%m-%d') for m in milestones]
            labels = [m['label'] for m in milestones]

            ax.plot(dates, [1] * len(dates), 'o-', markersize=10, linewidth=2)

            for i, (date, label) in enumerate(zip(dates, labels)):
                ax.annotate(
                    label,
                    (date, 1),
                    xytext=(0, 20 if i % 2 == 0 else -20),
                    textcoords='offset points',
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5)
                )

            ax.set_ylim(0.5, 1.5)
            ax.set_yticks([])
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
            plt.xticks(rotation=45)

            if title:
                ax.set_title(title, fontsize=14, fontweight='bold')

            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            return output_path

        except Exception as e:
            print(f"Error creating timeline: {e}")
            return ""
