"""
AI conversation module for interactive presentation creation.

This module provides conversation flow management for AI-assisted
presentation generation.
"""

from typing import Dict, List, Any, Optional
import os


class PresentationConversation:
    """
    Manages AI conversation flow for presentation creation.

    This class coordinates the conversation between the user and AI
    to gather requirements and generate presentations.

    Attributes:
        instruction_path: Path to AI instruction file
        conversation_history: History of conversation exchanges
        requirements: Gathered presentation requirements
    """

    def __init__(self, instruction_path: str = "instructions/PROJECT.md"):
        """
        Initialize the conversation manager.

        Args:
            instruction_path: Path to AI instruction markdown file
        """
        self.instruction_path = instruction_path
        self.conversation_history: List[Dict[str, str]] = []
        self.requirements: Dict[str, Any] = {}
        self.presentation_spec: Optional[Dict[str, Any]] = None

    def start_brief(self) -> Dict[str, Any]:
        """
        Begin initial requirements gathering conversation.

        Returns:
            Dictionary with conversation prompts and structure
        """
        initial_questions = {
            'purpose': 'What is the purpose of this presentation?',
            'audience': 'Who is the target audience? (engineers/business/general)',
            'duration': 'How long is the presentation? (in minutes)',
            'topics': 'What are the main topics to cover?',
            'language': 'Language preference? (ja/en)',
            'style': 'Presentation style? (technical/business/academic)'
        }

        return {
            'phase': 'requirements_gathering',
            'questions': initial_questions,
            'instructions': 'Please answer the questions above to help design your presentation.'
        }

    def propose_structure(self, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        AI proposes slide structure based on requirements.

        Args:
            requirements: Gathered requirements dictionary

        Returns:
            Proposed presentation structure
        """
        self.requirements = requirements

        # Basic structure proposal
        duration = requirements.get('duration', 15)
        slides_count = max(8, min(20, duration // 2))  # Rough estimate

        structure = {
            'presentation': {
                'title': requirements.get('title', 'Presentation'),
                'author': requirements.get('author', ''),
                'duration': duration,
                'slide_count': slides_count,
                'language': requirements.get('language', 'ja'),
                'theme': requirements.get('style', 'corporate')
            },
            'slides': [
                {'type': 'title', 'title': 'Title Slide'},
                {'type': 'content', 'title': 'Overview', 'layout': 'text'},
                # Add more based on topics...
            ]
        }

        self.presentation_spec = structure
        return structure

    def refine_content(self, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """
        Iteratively refine content based on user feedback.

        Args:
            feedback: User feedback on the proposed structure

        Returns:
            Updated presentation structure
        """
        if not self.presentation_spec:
            return {}

        # Apply feedback to presentation spec
        # This is a placeholder for actual refinement logic

        return self.presentation_spec

    def generate_presentation(self) -> Optional[str]:
        """
        Generate final presentation from conversation.

        Returns:
            Path to generated presentation file or None
        """
        if not self.presentation_spec:
            print("Error: No presentation specification available")
            return None

        # This would trigger the actual presentation generation
        # Placeholder for now
        print("Generating presentation based on conversation...")

        return None  # Will return actual path when implemented

    def save_conversation(self, filename: str = "conversation_history.json"):
        """
        Save conversation history to file.

        Args:
            filename: Output filename for conversation history
        """
        import json

        history_data = {
            'conversation': self.conversation_history,
            'requirements': self.requirements,
            'presentation_spec': self.presentation_spec
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(history_data, f, indent=2, ensure_ascii=False)

        print(f"Conversation saved to: {filename}")

    def load_conversation(self, filename: str):
        """
        Load conversation history from file.

        Args:
            filename: Input filename for conversation history
        """
        import json

        with open(filename, 'r', encoding='utf-8') as f:
            history_data = json.load(f)

        self.conversation_history = history_data.get('conversation', [])
        self.requirements = history_data.get('requirements', {})
        self.presentation_spec = history_data.get('presentation_spec')

        print(f"Conversation loaded from: {filename}")
