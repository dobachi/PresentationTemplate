#!/usr/bin/env python3
"""
Architecture Diagram Examples

This example demonstrates how to create various architecture diagrams
for presentations.
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.diagrams.architecture import ArchitectureDiagram


def example_three_layer_architecture():
    """Create a 3-layer data space architecture diagram."""
    print("Creating 3-layer architecture diagram...")

    arch_diagram = ArchitectureDiagram(language='en', output_dir='output/examples')

    diagram_path = arch_diagram.create_three_layer_architecture(
        layers={
            'application': ['Web App', 'Mobile App', 'Admin Portal'],
            'service': ['API Gateway', 'Auth Service', 'Data Catalog', 'Search Service'],
            'data': ['PostgreSQL DB', 'Object Storage', 'Cache']
        },
        filename='three_layer_architecture'
    )

    print(f"✓ Generated: {diagram_path}")
    return diagram_path


def example_cloud_architecture():
    """Create a cloud architecture diagram."""
    print("Creating cloud architecture diagram...")

    arch_diagram = ArchitectureDiagram(language='en', output_dir='output/examples')

    diagram_path = arch_diagram.create_cloud_architecture(
        components=[
            {'type': 'elb', 'name': 'Load Balancer'},
            {'type': 'ec2', 'name': 'Web Server 1'},
            {'type': 'ec2', 'name': 'Web Server 2'},
            {'type': 'rds', 'name': 'Database'},
            {'type': 's3', 'name': 'File Storage'},
        ],
        connections=[
            {'from': 'Load Balancer', 'to': 'Web Server 1', 'label': 'HTTP'},
            {'from': 'Load Balancer', 'to': 'Web Server 2', 'label': 'HTTP'},
            {'from': 'Web Server 1', 'to': 'Database', 'label': 'SQL'},
            {'from': 'Web Server 2', 'to': 'Database', 'label': 'SQL'},
            {'from': 'Web Server 1', 'to': 'File Storage', 'label': 'S3 API'},
            {'from': 'Web Server 2', 'to': 'File Storage', 'label': 'S3 API'},
        ],
        filename='cloud_architecture'
    )

    print(f"✓ Generated: {diagram_path}")
    return diagram_path


def example_international_interop():
    """Create international data space interoperability diagram."""
    print("Creating international interoperability diagram...")

    arch_diagram = ArchitectureDiagram(language='en', output_dir='output/examples')

    diagram_path = arch_diagram.create_international_interop_diagram(
        filename='international_interop'
    )

    print(f"✓ Generated: {diagram_path}")
    return diagram_path


def example_microservices():
    """Create a microservices architecture diagram."""
    print("Creating microservices architecture diagram...")

    arch_diagram = ArchitectureDiagram(language='en', output_dir='output/examples')

    diagram_path = arch_diagram.create_microservices(
        services=[
            {'name': 'User Service'},
            {'name': 'Product Service'},
            {'name': 'Order Service'},
            {'name': 'Payment Service'},
            {'name': 'Notification Service'},
        ],
        dependencies=[
            {'from': 'User Service', 'to': 'Order Service', 'type': 'sync'},
            {'from': 'Product Service', 'to': 'Order Service', 'type': 'sync'},
            {'from': 'Order Service', 'to': 'Payment Service', 'type': 'sync'},
            {'from': 'Payment Service', 'to': 'Notification Service', 'type': 'async'},
            {'from': 'Order Service', 'to': 'Notification Service', 'type': 'async'},
        ],
        filename='microservices_architecture'
    )

    print(f"✓ Generated: {diagram_path}")
    return diagram_path


def main():
    """Run all examples."""
    print("=" * 60)
    print("Architecture Diagram Examples")
    print("=" * 60)
    print()

    # Create output directory
    os.makedirs('output/examples', exist_ok=True)

    # Run examples
    example_three_layer_architecture()
    print()

    example_cloud_architecture()
    print()

    example_international_interop()
    print()

    example_microservices()
    print()

    print("=" * 60)
    print("All examples completed!")
    print("Check output/examples/ directory for generated diagrams")
    print("=" * 60)


if __name__ == '__main__':
    main()
