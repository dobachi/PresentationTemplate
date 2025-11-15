"""
Network diagram generation module.

This module provides functionality for creating network topology
diagrams using networkx and matplotlib.
"""

import os
from typing import Dict, List, Any, Optional


class NetworkDiagram:
    """
    Class for creating network diagrams.

    Uses networkx and matplotlib to create network topology,
    connectivity, and relationship diagrams.

    Attributes:
        theme: Theme configuration dictionary
        language: Language code for labels
        output_dir: Directory for saving generated diagrams
    """

    def __init__(
        self,
        theme: Optional[Dict[str, Any]] = None,
        language: str = "ja",
        output_dir: str = "output/diagrams"
    ):
        """
        Initialize the NetworkDiagram generator.

        Args:
            theme: Theme configuration dictionary
            language: Language code ('ja' or 'en')
            output_dir: Output directory for diagrams
        """
        self.theme = theme or {}
        self.language = language
        self.output_dir = output_dir

        os.makedirs(output_dir, exist_ok=True)

    def _get_label(self, key: str, en: str, ja: str) -> str:
        """Get localized label."""
        return ja if self.language == 'ja' else en

    def _configure_matplotlib_fonts(self):
        """Configure matplotlib for Japanese/English fonts."""
        try:
            import matplotlib.pyplot as plt

            if self.language == 'ja':
                plt.rcParams['font.sans-serif'] = ['Meiryo', 'Hiragino Sans', 'Yu Gothic', 'DejaVu Sans']
            else:
                plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

            plt.rcParams['font.family'] = 'sans-serif'
            plt.rcParams['axes.unicode_minus'] = False

        except Exception as e:
            print(f"Warning: Could not configure fonts: {e}")

    def create_network_topology(
        self,
        nodes: List[Dict[str, Any]],
        edges: List[Dict[str, Any]],
        filename: str = "network_topology"
    ) -> str:
        """
        Create a network topology diagram.

        Args:
            nodes: List of network nodes
                   Each node: {'id': str, 'label': str, 'type': str}
            edges: List of network connections
                   Each edge: {'from': str, 'to': str, 'weight': int (optional)}
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            import networkx as nx
            import matplotlib.pyplot as plt

            self._configure_matplotlib_fonts()

            output_path = os.path.join(self.output_dir, filename + ".png")

            # Create graph
            G = nx.Graph()

            # Add nodes
            for node in nodes:
                node_id = node.get('id', '')
                node_type = node.get('type', 'default')
                G.add_node(node_id, node_type=node_type)

            # Add edges
            for edge in edges:
                from_node = edge.get('from', '')
                to_node = edge.get('to', '')
                weight = edge.get('weight', 1)
                label = edge.get('label', '')

                G.add_edge(from_node, to_node, weight=weight, label=label)

            # Draw
            fig, ax = plt.subplots(figsize=(12, 8))

            pos = nx.spring_layout(G, k=2, iterations=50)

            # Draw nodes with different colors based on type
            node_types = set(nx.get_node_attributes(G, 'node_type').values())
            colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']

            for i, node_type in enumerate(node_types):
                node_list = [n for n, attr in G.nodes(data=True)
                           if attr.get('node_type') == node_type]
                nx.draw_networkx_nodes(
                    G, pos,
                    nodelist=node_list,
                    node_color=colors[i % len(colors)],
                    node_size=3000,
                    ax=ax
                )

            # Draw edges
            nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, ax=ax)

            # Draw labels
            nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)

            # Draw edge labels if present
            edge_labels = nx.get_edge_attributes(G, 'label')
            if edge_labels:
                nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8, ax=ax)

            plt.axis('off')
            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()

            return output_path

        except ImportError as e:
            print(f"Error: Required library not installed: {e}")
            print("Install with: pip install networkx matplotlib")
            return ""

        except Exception as e:
            print(f"Error creating network topology: {e}")
            return ""

    def create_interoperability_network(
        self,
        regions: List[str],
        dataspaces: Dict[str, List[str]],
        connections: List[Dict[str, str]],
        filename: str = "interoperability_network"
    ) -> str:
        """
        Create international data space interoperability network.

        Args:
            regions: List of region names
            dataspaces: Dictionary mapping regions to data spaces
            connections: List of connection specifications
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            import networkx as nx
            import matplotlib.pyplot as plt

            self._configure_matplotlib_fonts()

            output_path = os.path.join(self.output_dir, filename + ".png")

            # Create graph
            G = nx.Graph()

            # Add region nodes
            for region in regions:
                G.add_node(region, node_type='region', size=5000)

            # Add dataspace nodes
            for region, spaces in dataspaces.items():
                for space in spaces:
                    G.add_node(space, node_type='dataspace', size=3000)
                    # Connect dataspace to its region
                    G.add_edge(region, space, edge_type='regional')

            # Add interoperability connections
            for conn in connections:
                from_node = conn.get('from', '')
                to_node = conn.get('to', '')
                label = conn.get('label', '')

                G.add_edge(from_node, to_node, edge_type='interop', label=label)

            # Draw
            fig, ax = plt.subplots(figsize=(14, 10))

            pos = nx.spring_layout(G, k=3, iterations=50)

            # Draw nodes
            region_nodes = [n for n, attr in G.nodes(data=True)
                          if attr.get('node_type') == 'region']
            dataspace_nodes = [n for n, attr in G.nodes(data=True)
                             if attr.get('node_type') == 'dataspace']

            nx.draw_networkx_nodes(
                G, pos,
                nodelist=region_nodes,
                node_color='lightcoral',
                node_size=5000,
                node_shape='s',
                ax=ax
            )

            nx.draw_networkx_nodes(
                G, pos,
                nodelist=dataspace_nodes,
                node_color='lightblue',
                node_size=3000,
                ax=ax
            )

            # Draw edges with different styles
            regional_edges = [(u, v) for u, v, attr in G.edges(data=True)
                            if attr.get('edge_type') == 'regional']
            interop_edges = [(u, v) for u, v, attr in G.edges(data=True)
                           if attr.get('edge_type') == 'interop']

            nx.draw_networkx_edges(
                G, pos,
                edgelist=regional_edges,
                width=2,
                alpha=0.5,
                style='solid',
                ax=ax
            )

            nx.draw_networkx_edges(
                G, pos,
                edgelist=interop_edges,
                width=3,
                alpha=0.7,
                style='dashed',
                edge_color='red',
                ax=ax
            )

            # Draw labels
            nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', ax=ax)

            # Draw edge labels
            edge_labels = nx.get_edge_attributes(G, 'label')
            if edge_labels:
                nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=9, ax=ax)

            title = self._get_label(
                'interop_title',
                'Data Space Interoperability Network',
                'データスペース相互運用ネットワーク'
            )
            plt.title(title, fontsize=16, fontweight='bold')

            plt.axis('off')
            plt.tight_layout()
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()

            return output_path

        except ImportError as e:
            print(f"Error: Required library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating interoperability network: {e}")
            return ""
