"""
Version manager for tracking presentation iterations.

Manages presentation versions through iterative refinement process.
"""

import os
import shutil
from datetime import datetime
from typing import Optional, List, Dict
from pathlib import Path


class VersionManager:
    """
    Manages presentation versions/iterations.

    Saves each iteration with timestamp and descriptive notes,
    allowing users to refine presentations progressively.
    """

    def __init__(self, base_name: str = "presentation", versions_dir: str = "versions"):
        """
        Initialize version manager.

        Args:
            base_name: Base name for presentation files
            versions_dir: Directory to store versioned files
        """
        self.base_name = base_name
        self.versions_dir = versions_dir
        self.versions: List[Dict[str, str]] = []

        # Create versions directory
        os.makedirs(versions_dir, exist_ok=True)

        # Load existing versions
        self._load_versions()

    def _load_versions(self):
        """Load existing versions from directory."""
        if not os.path.exists(self.versions_dir):
            return

        # Find all versioned files for this presentation
        pattern = f"{self.base_name}_v*"

        for file_path in Path(self.versions_dir).glob(f"{pattern}.pptx"):
            # Parse version info from filename
            # Format: basename_v{num}_{timestamp}_{note}.pptx
            filename = file_path.stem
            parts = filename.split('_')

            if len(parts) >= 3:
                version_num = parts[1].replace('v', '')
                timestamp = '_'.join(parts[2:4]) if len(parts) >= 4 else parts[2]
                note = '_'.join(parts[4:]) if len(parts) > 4 else ''

                self.versions.append({
                    'version': int(version_num) if version_num.isdigit() else 0,
                    'timestamp': timestamp,
                    'note': note.replace('-', ' '),
                    'path': str(file_path)
                })

        # Sort by version number
        self.versions.sort(key=lambda v: v['version'])

    def save_version(
        self,
        presentation_path: str,
        iteration_note: str = "update"
    ) -> str:
        """
        Save current version with timestamp and note.

        Args:
            presentation_path: Path to current presentation file
            iteration_note: Descriptive note for this iteration

        Returns:
            Path to saved version file

        Example:
            versions/my_presentation_v1_2025-01-15_10-30_initial.pptx
            versions/my_presentation_v2_2025-01-15_10-45_added-diagrams.pptx
        """
        if not os.path.exists(presentation_path):
            raise FileNotFoundError(f"Presentation file not found: {presentation_path}")

        # Get next version number
        next_version = len(self.versions) + 1

        # Create timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')

        # Clean note for filename
        clean_note = iteration_note.lower().replace(' ', '-')

        # Create version filename
        version_filename = f"{self.base_name}_v{next_version}_{timestamp}_{clean_note}.pptx"
        version_path = os.path.join(self.versions_dir, version_filename)

        # Copy file
        shutil.copy2(presentation_path, version_path)

        # Add to versions list
        self.versions.append({
            'version': next_version,
            'timestamp': timestamp,
            'note': iteration_note,
            'path': version_path
        })

        print(f"Saved version {next_version}: {version_path}")
        return version_path

    def load_version(self, version_number: Optional[int] = None) -> Optional[str]:
        """
        Load a specific version.

        Args:
            version_number: Version to load (default: latest)

        Returns:
            Path to version file or None if not found
        """
        if not self.versions:
            return None

        if version_number is None:
            # Return latest version
            return self.versions[-1]['path']

        # Find specific version
        for v in self.versions:
            if v['version'] == version_number:
                return v['path']

        return None

    def get_latest_version(self) -> Optional[Dict[str, str]]:
        """
        Get latest version info.

        Returns:
            Dictionary with version info or None
        """
        if not self.versions:
            return None

        return self.versions[-1]

    def list_versions(self) -> List[Dict[str, str]]:
        """
        List all versions.

        Returns:
            List of version dictionaries
        """
        return self.versions

    def compare_versions(self, v1: int, v2: int) -> Dict[str, any]:
        """
        Compare two versions.

        Args:
            v1: First version number
            v2: Second version number

        Returns:
            Dictionary with comparison info
        """
        version1 = next((v for v in self.versions if v['version'] == v1), None)
        version2 = next((v for v in self.versions if v['version'] == v2), None)

        if not version1 or not version2:
            return {'error': 'Version not found'}

        # Basic comparison (file size, modification time)
        path1 = version1['path']
        path2 = version2['path']

        size1 = os.path.getsize(path1) if os.path.exists(path1) else 0
        size2 = os.path.getsize(path2) if os.path.exists(path2) else 0

        return {
            'v1': version1,
            'v2': version2,
            'size_diff': size2 - size1,
            'size_change_percent': ((size2 - size1) / size1 * 100) if size1 > 0 else 0
        }

    def rollback(self, version_number: int, output_path: str) -> bool:
        """
        Rollback to a previous version.

        Args:
            version_number: Version to rollback to
            output_path: Where to copy the rolled-back version

        Returns:
            True if successful, False otherwise
        """
        version_path = self.load_version(version_number)

        if not version_path or not os.path.exists(version_path):
            print(f"Error: Version {version_number} not found")
            return False

        try:
            shutil.copy2(version_path, output_path)
            print(f"Rolled back to version {version_number}: {version_path}")
            print(f"Saved to: {output_path}")
            return True
        except Exception as e:
            print(f"Error rolling back: {e}")
            return False

    def create_backup(self, presentation_path: str) -> str:
        """
        Create a backup before making changes.

        Args:
            presentation_path: Path to presentation file

        Returns:
            Path to backup file
        """
        return self.save_version(presentation_path, "backup")

    def print_version_history(self):
        """Print version history in a readable format."""
        if not self.versions:
            print("No versions found")
            return

        print("=" * 70)
        print(f"Version History for '{self.base_name}'")
        print("=" * 70)

        for v in self.versions:
            print(f"\nVersion {v['version']}")
            print(f"  Timestamp: {v['timestamp']}")
            print(f"  Note:      {v['note']}")
            print(f"  Path:      {v['path']}")

            if os.path.exists(v['path']):
                size_mb = os.path.getsize(v['path']) / (1024 * 1024)
                print(f"  Size:      {size_mb:.2f} MB")

        print("=" * 70)
