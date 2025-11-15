#!/usr/bin/env python3
"""
Full Presentation Example

This example demonstrates creating a complete presentation about
Data Space International Interoperability.
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.presentation import PresentationBuilder
from src.diagrams.architecture import ArchitectureDiagram
from src.diagrams.network import NetworkDiagram
from src.charts.statistical import StatisticalChart


def create_data_space_presentation():
    """Create a complete presentation about data space interoperability."""

    print("Creating Data Space International Interoperability presentation...")
    print()

    # Create output directories
    os.makedirs('output/presentations', exist_ok=True)
    os.makedirs('output/diagrams', exist_ok=True)
    os.makedirs('output/charts', exist_ok=True)

    # Initialize presentation builder
    builder = PresentationBuilder(theme='corporate', language='en')
    builder.set_metadata(
        title="Data Space International Interoperability",
        author="Dobachi",
        subject="Data Space Architecture"
    )

    # Slide 1: Title
    print("Adding title slide...")
    builder.add_title_slide(
        title="Data Space International Interoperability",
        subtitle="Japan-Europe Collaboration: Status and Prospects"
    )

    # Slide 2: Introduction
    print("Adding introduction slide...")
    builder.add_text_slide(
        title="Introduction",
        bullets=[
            "Data spaces enable secure data sharing across organizations",
            "International collaboration is key to success",
            "Focus on Japan (Ouranos) and Europe (Gaia-X) interoperability",
            "Technical and governance challenges"
        ]
    )

    # Slide 3: Data Space 3-Layer Architecture
    print("Generating 3-layer architecture diagram...")
    arch_diagram = ArchitectureDiagram(language='en', output_dir='output/diagrams')
    diagram_path = arch_diagram.create_three_layer_architecture(
        layers={
            'application': ['Data Consumer Apps', 'Data Provider Apps', 'Admin Tools'],
            'service': ['API Gateway', 'Identity & Auth', 'Data Catalog', 'Usage Control'],
            'data': ['Metadata Store', 'Data Storage', 'Trust Framework']
        },
        filename='dataspace_3layer'
    )

    builder.add_diagram_slide(
        title="Data Space 3-Layer Architecture",
        diagram_path=diagram_path,
        notes="The 3-layer architecture provides separation of concerns and modularity"
    )

    # Slide 4: Interoperability Challenges
    print("Adding challenges slide...")
    builder.add_text_slide(
        title="Interoperability Challenges",
        bullets=[
            "Technical Standards: API protocols, data formats, metadata schemas",
            "Governance: Policy alignment, legal frameworks, compliance",
            "Trust: Identity management, authentication, authorization",
            "Data Sovereignty: Respecting national and regional regulations"
        ]
    )

    # Slide 5: International Interoperability Network
    print("Generating interoperability network diagram...")
    network_diagram = NetworkDiagram(language='en', output_dir='output/diagrams')
    network_path = network_diagram.create_interoperability_network(
        regions=['Japan', 'Europe'],
        dataspaces={
            'Japan': ['Ouranos', 'Other JP Data Spaces'],
            'Europe': ['Gaia-X', 'Other EU Data Spaces']
        },
        connections=[
            {'from': 'Ouranos', 'to': 'Gaia-X', 'label': 'Standard Protocols'},
            {'from': 'Ouranos', 'to': 'Other EU Data Spaces', 'label': 'API Gateway'},
        ],
        filename='interop_network'
    )

    builder.add_diagram_slide(
        title="International Interoperability Network",
        diagram_path=network_path,
        notes="Network showing connections between Japan and Europe data spaces"
    )

    # Slide 6: Adoption Trends
    print("Generating adoption trend chart...")
    chart = StatisticalChart(language='en', output_dir='output/charts')
    chart_path = chart.create_line_chart(
        data={
            'x': [2020, 2021, 2022, 2023, 2024],
            'y_ouranos': [10, 25, 45, 80, 120],
            'y_gaiax': [30, 60, 95, 140, 200]
        },
        labels={
            'x_axis': 'Year',
            'y_axis': 'Number of Participants',
            'y_ouranos': 'Ouranos (Japan)',
            'y_gaiax': 'Gaia-X (Europe)'
        },
        title='Data Space Adoption Trend (2020-2024)',
        filename='adoption_trend'
    )

    builder.add_chart_slide(
        title="Adoption Trends",
        chart_path=chart_path,
        notes="Both ecosystems show steady growth in participation"
    )

    # Slide 7: Technical Standards Comparison
    print("Adding standards comparison slide...")
    builder.add_text_slide(
        title="Technical Standards Comparison",
        bullets=[
            "Authentication: Both use OAuth 2.0 / OpenID Connect ✓",
            "Data Format: JSON-LD for metadata ✓",
            "API Protocol: REST APIs with OpenAPI specs ✓",
            "Trust Framework: Different but compatible approaches △",
            "Metadata Schema: Alignment in progress (DCAT-AP) △"
        ]
    )

    # Slide 8: Key Success Factors
    print("Adding success factors slide...")
    builder.add_text_slide(
        title="Key Success Factors",
        bullets=[
            "Continuous dialogue between stakeholders",
            "Incremental standardization approach",
            "Pilot projects demonstrating interoperability",
            "Shared governance principles",
            "Open source tooling and reference implementations"
        ]
    )

    # Slide 9: Summary
    print("Adding summary slide...")
    builder.add_text_slide(
        title="Summary",
        bullets=[
            "Japan-Europe data space interoperability is advancing steadily",
            "Technical standards are converging (OAuth, JSON-LD, REST APIs)",
            "Governance and trust frameworks need continued alignment",
            "Future challenges: Data sovereignty, cross-border data flows",
            "Next steps: Pilot implementations, standard refinement"
        ]
    )

    # Save presentation
    output_path = 'output/presentations/DataSpace_Interoperability.pptx'
    print()
    print("Saving presentation...")
    builder.save(output_path)

    print()
    print("=" * 60)
    print("✓ Presentation created successfully!")
    print(f"✓ Location: {output_path}")
    print(f"✓ Slides: 9")
    print(f"✓ Diagrams: 2 (architecture + network)")
    print(f"✓ Charts: 1 (line chart)")
    print("=" * 60)


def main():
    """Main function."""
    print("=" * 60)
    print("Full Presentation Example")
    print("Data Space International Interoperability")
    print("=" * 60)
    print()

    try:
        create_data_space_presentation()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
