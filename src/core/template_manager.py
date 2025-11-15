"""
Template manager module for handling PowerPoint templates.

This module provides functionality for loading and managing PowerPoint
template files.
"""

import os
from typing import Optional
from pptx import Presentation


class TemplateManager:
    """
    Manager class for PowerPoint templates.

    Handles loading and validation of template files.

    Attributes:
        template_path: Path to the template file
        template: Loaded Presentation template (if available)
    """

    def __init__(self, template_path: Optional[str] = None):
        """
        Initialize the TemplateManager.

        Args:
            template_path: Optional path to PowerPoint template file (.pptx)
        """
        self.template_path = template_path
        self.template = None

        if template_path:
            self.load_template(template_path)

    def load_template(self, template_path: str) -> bool:
        """
        Load a PowerPoint template file.

        Args:
            template_path: Path to template file

        Returns:
            True if successfully loaded, False otherwise
        """
        if not os.path.exists(template_path):
            print(f"Warning: Template file not found: {template_path}")
            return False

        if not template_path.endswith('.pptx'):
            print(f"Warning: Template file must be .pptx format")
            return False

        try:
            self.template = Presentation(template_path)
            self.template_path = template_path
            print(f"Template loaded: {template_path}")
            return True
        except Exception as e:
            print(f"Error loading template: {e}")
            return False

    def get_template(self) -> Optional[Presentation]:
        """
        Get the loaded template.

        Returns:
            Presentation object if template is loaded, None otherwise
        """
        return self.template

    def list_layouts(self):
        """
        List available slide layouts in the template.

        Prints layout names and indices.
        """
        if not self.template:
            print("No template loaded")
            return

        print(f"Available layouts in {self.template_path}:")
        for i, layout in enumerate(self.template.slide_layouts):
            print(f"  [{i}] {layout.name}")

    def validate_template(self) -> bool:
        """
        Validate that the template has required layouts.

        Returns:
            True if template is valid, False otherwise
        """
        if not self.template:
            return False

        # Check for minimum required layouts
        required_layouts = ['Title Slide', 'Title and Content', 'Blank']

        available_layouts = [layout.name for layout in self.template.slide_layouts]

        for required in required_layouts:
            if required not in available_layouts:
                print(f"Warning: Required layout '{required}' not found in template")
                return False

        return True
