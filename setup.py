"""Setup script for PresentationTemplate package."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    long_description = readme_file.read_text(encoding='utf-8')

setup(
    name="presentation-generator",
    version="0.1.0",
    author="Dobachi",
    description="AI-Assisted Graphical Presentation Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dobachi/PresentationTemplate",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Office Suites",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-pptx>=0.6.21",
        "diagrams>=0.23.0",
        "graphviz>=0.20.0",
        "networkx>=3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "plotly>=5.14.0",
        "Pillow>=10.0.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "PyYAML>=6.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "python-dateutil>=2.8.0",
    ],
    entry_points={
        "console_scripts": [
            "presentation-gen=src.cli:cli",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.md"],
    },
)
