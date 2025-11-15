# AI-Assisted Graphical Presentation Generator

English | [日本語](README.md)

A Python-based presentation generation framework that works with **AI_Instruction_Kits** to enable AI-assisted creation of professional, graphical presentations for technical and business content.

## Features

- **AI-Assisted Conversation Mode**: Create presentations through natural language dialogue
- **Multiple Diagram Types**: Architecture diagrams, flowcharts, network diagrams using `diagrams`, `graphviz`, and `networkx`
- **Statistical Charts**: Line charts, bar charts, scatter plots, pie charts using `matplotlib` and `seaborn`
- **Bilingual Support**: Japanese and English presentations with proper font handling
- **Theme System**: Corporate, technical, and academic themes
- **PowerPoint Generation**: Professional .pptx files with `python-pptx`

## Installation

### Prerequisites

- Python 3.8 or higher
- Graphviz (for flowcharts)
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer (recommended)

### Install uv (Recommended)

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (with pip):**
```bash
pip install uv
```

### Install Graphviz

**Ubuntu/Debian:**
```bash
sudo apt-get install graphviz
```

**macOS:**
```bash
brew install graphviz
```

**Windows:**
Download from https://graphviz.org/download/

### Install Package

#### Option 1: Using uv (Recommended - Fast)

```bash
# Clone repository
git clone https://github.com/dobachi/PresentationTemplate.git
cd PresentationTemplate

# Initialize AI_Instruction_Kits submodule
git submodule update --init --recursive

# Create virtual environment and install dependencies with uv
uv venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate    # On Windows

# Install dependencies
uv pip install -r requirements.txt

# Install package in development mode
uv pip install -e .
```

#### Option 2: Using Traditional venv + pip

```bash
# Clone repository
git clone https://github.com/dobachi/PresentationTemplate.git
cd PresentationTemplate

# Initialize AI_Instruction_Kits submodule
git submodule update --init --recursive

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/macOS
# venv\Scripts\activate    # On Windows

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

## Quick Start

### Method 1: AI-Assisted Mode (Recommended)

Talk to Claude directly using the CLAUDE.md instruction file:

```
I want to create a 15-minute presentation about Data Space International
Interoperability, focusing on Japan-Europe collaboration (Ouranos and Gaia-X).
Target audience is technical. Language: English.
```

Claude will:
1. Ask clarifying questions
2. Propose slide structure
3. Generate diagrams automatically
4. Create the PowerPoint file

### Method 2: Python API

```python
from src.core.presentation import PresentationBuilder
from src.diagrams.architecture import ArchitectureDiagram
from src.charts.statistical import StatisticalChart

# Create builder
builder = PresentationBuilder(theme='corporate', language='en')

# Add title slide
builder.add_title_slide(
    title="Data Space International Interoperability",
    subtitle="Japan-Europe Collaboration"
)

# Generate and add architecture diagram
arch_diagram = ArchitectureDiagram(language='en')
diagram_path = arch_diagram.create_three_layer_architecture(
    layers={
        'application': ['App 1', 'App 2', 'App 3'],
        'service': ['API Gateway', 'Auth Service', 'Data Catalog'],
        'data': ['Metadata DB', 'Data Storage', 'Object Store']
    }
)
builder.add_diagram_slide(
    title="Data Space 3-Layer Architecture",
    diagram_path=diagram_path
)

# Generate and add chart
chart = StatisticalChart(language='en')
chart_path = chart.create_line_chart(
    data={
        'x': [2020, 2021, 2022, 2023, 2024],
        'y_ouranos': [10, 25, 45, 80, 120],
        'y_gaiax': [30, 60, 95, 140, 200]
    },
    labels={
        'x_axis': 'Year',
        'y_axis': 'Adoption Rate',
        'y_ouranos': 'Ouranos',
        'y_gaiax': 'Gaia-X'
    },
    title='Data Space Adoption Trend'
)
builder.add_chart_slide(
    title="Adoption Trends",
    chart_path=chart_path
)

# Save presentation
builder.save('output/DataSpace_Interoperability.pptx')
```

### Method 3: YAML Definition

Create a YAML file:

```yaml
presentation:
  title: "Data Space Architecture"
  author: "Dobachi"
  language: "en"
  theme: "corporate"

slides:
  - type: title
    title: "Data Space Architecture"
    subtitle: "Overview and Components"

  - type: content
    title: "Introduction"
    layout: "text"
    bullets:
      - "What is Data Space"
      - "Why it matters"
      - "Key components"
```

Generate:

```python
builder = PresentationBuilder()
builder.load_definition('my_presentation.yaml')
builder.build_from_definition(builder.load_definition('my_presentation.yaml'))
builder.save('output.pptx')
```

## Supported Diagram Types

### Architecture Diagrams

- 3-layer architecture (Data/Service/Application)
- Cloud architecture (AWS, Azure, GCP)
- Microservices architecture
- International interoperability (Ouranos ↔ Gaia-X)

### Flowcharts

- Process flows
- Decision trees
- Data flow diagrams

### Network Diagrams

- Network topology
- Interoperability networks
- Connectivity diagrams

### Statistical Charts

- Line charts
- Bar charts (vertical/horizontal)
- Scatter plots
- Pie charts
- Stacked bar charts

## Bilingual Support

### Japanese Presentation

```python
builder = PresentationBuilder(theme='corporate', language='ja')
builder.set_fonts(
    title_font='Meiryo',
    body_font='Meiryo'
)
```

### English Presentation

```python
builder = PresentationBuilder(theme='corporate', language='en')
builder.set_fonts(
    title_font='Arial',
    body_font='Arial'
)
```

### Mixed Japanese-English

```python
builder = PresentationBuilder(theme='corporate', language='ja_en')
builder.add_title_slide(
    title="Data Space Architecture",
    subtitle="データスペースアーキテクチャ"
)
```

## Themes

Three built-in themes:

- **Corporate**: Professional blue theme
- **Technical**: Technical with dark accents
- **Academic**: Academic style

Custom themes can be created in `config/themes/`.

## Examples

See the `examples/` directory for:

- `architecture_example.py` - Architecture diagram examples
- `full_presentation_example.py` - Complete presentation example
- `example_conversation.md` - Sample AI conversation

## AI Instruction Files

The project includes specialized AI instruction modules in `instructions/modules/`:

- `presentation_designer.md` - Conversation guide for design
- `diagram_generator.md` - Diagram creation instructions
- `presentation_workflow.md` - End-to-end workflow

These work with the [AI_Instruction_Kits](https://github.com/dobachi/AI_Instruction_Kits) framework.

## Project Structure

```
PresentationTemplate/
├── src/
│   ├── core/           # Core presentation building
│   ├── diagrams/       # Diagram generation
│   ├── charts/         # Chart generation
│   └── ai/             # AI conversation flow
├── config/
│   └── themes/         # Theme configurations
├── instructions/
│   ├── ai_instruction_kits/  # Submodule
│   └── modules/        # Custom instruction modules
├── examples/           # Usage examples
└── templates/          # PowerPoint templates
```

## Troubleshooting

If you encounter issues, see the [Troubleshooting Guide](TROUBLESHOOTING.en.md).

Common issues:
- **Graphviz errors**: Ensure Graphviz is installed on your system
- **Japanese font issues**: Meiryo or fallback fonts must be installed
- **Dependency errors**: Reinstall with `uv pip install -r requirements.txt`

## License

MIT License

## Contributing

Contributions welcome! Please see CONTRIBUTING.md for guidelines.

## Author

Dobachi

## Acknowledgments

- Built on top of [AI_Instruction_Kits](https://github.com/dobachi/AI_Instruction_Kits)
- Uses [python-pptx](https://python-pptx.readthedocs.io/)
- Diagrams powered by [diagrams](https://diagrams.mingrammer.com/)
