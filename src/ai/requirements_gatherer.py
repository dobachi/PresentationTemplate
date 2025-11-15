"""
Requirements gatherer module.

Extract structured requirements from natural language conversation.
"""

from typing import Dict, List, Any


class RequirementsGatherer:
    """
    Extract structured requirements from natural language conversation.

    Parses conversation to identify presentation requirements including
    purpose, audience, topics, and constraints.
    """

    def __init__(self):
        """Initialize the requirements gatherer."""
        self.required_fields = ['purpose', 'audience', 'duration', 'topics']
        self.optional_fields = ['style', 'language', 'examples', 'constraints']

    def parse_conversation(self, conversation_history: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Parse conversation to extract requirements.

        Args:
            conversation_history: List of conversation exchanges

        Returns:
            Structured requirements dictionary
        """
        requirements = {
            'purpose': '',
            'audience': 'technical',
            'duration': 15,
            'topics': [],
            'style': 'corporate',
            'language': 'ja',
            'examples': [],
            'constraints': {}
        }

        # Placeholder for actual NLP parsing
        # In real implementation, this would analyze conversation text

        return requirements

    def validate_requirements(self, requirements: Dict[str, Any]) -> tuple[bool, List[str]]:
        """
        Ensure all necessary information is gathered.

        Args:
            requirements: Requirements dictionary to validate

        Returns:
            Tuple of (is_valid, missing_fields)
        """
        missing_fields = []

        for field in self.required_fields:
            if not requirements.get(field):
                missing_fields.append(field)

        is_valid = len(missing_fields) == 0

        return is_valid, missing_fields

    def suggest_missing_info(self, missing_fields: List[str]) -> Dict[str, str]:
        """
        Suggest questions for missing information.

        Args:
            missing_fields: List of missing field names

        Returns:
            Dictionary mapping fields to suggested questions
        """
        questions = {
            'purpose': 'What is the main purpose of this presentation?',
            'audience': 'Who is the target audience?',
            'duration': 'How long should the presentation be?',
            'topics': 'What topics should be covered?',
            'style': 'What style would you prefer? (technical/business/academic)',
            'language': 'Which language? (Japanese/English)'
        }

        return {field: questions.get(field, f'Please specify {field}')
                for field in missing_fields}
