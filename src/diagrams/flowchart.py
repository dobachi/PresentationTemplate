"""
Flowchart diagram generation module.

This module provides functionality for creating flowcharts and process
diagrams using graphviz.
"""

import os
from typing import Dict, List, Any, Optional


class FlowchartDiagram:
    """
    Class for creating flowchart diagrams.

    Uses graphviz to create process flows, decision trees, and
    algorithm flowcharts.

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
        Initialize the FlowchartDiagram generator.

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

    def create_process_flow(
        self,
        nodes: List[Dict[str, str]],
        edges: List[Dict[str, str]],
        filename: str = "process_flow"
    ) -> str:
        """
        Create a process flowchart.

        Args:
            nodes: List of node specifications
                   Each node: {'id': str, 'label': str, 'shape': str}
            edges: List of edge specifications
                   Each edge: {'from': str, 'to': str, 'label': str (optional)}
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            from graphviz import Digraph

            output_path = os.path.join(self.output_dir, filename)

            dot = Digraph(comment='Process Flow', format='png')
            dot.attr(rankdir='TB', size='8,6')
            dot.attr('node', fontname='Meiryo' if self.language == 'ja' else 'Arial')
            dot.attr('edge', fontname='Meiryo' if self.language == 'ja' else 'Arial')

            # Add nodes
            for node in nodes:
                node_id = node.get('id', '')
                label = node.get('label', '')
                shape = node.get('shape', 'box')

                dot.node(node_id, label, shape=shape)

            # Add edges
            for edge in edges:
                from_node = edge.get('from', '')
                to_node = edge.get('to', '')
                label = edge.get('label', '')

                if label:
                    dot.edge(from_node, to_node, label=label)
                else:
                    dot.edge(from_node, to_node)

            # Render
            dot.render(output_path, cleanup=True)

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: 'graphviz' library not installed: {e}")
            print("Install with: pip install graphviz")
            return ""

        except Exception as e:
            print(f"Error creating flowchart: {e}")
            return ""

    def create_decision_tree(
        self,
        root: Dict[str, Any],
        filename: str = "decision_tree"
    ) -> str:
        """
        Create a decision tree diagram.

        Args:
            root: Root node specification (recursive structure)
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            from graphviz import Digraph

            output_path = os.path.join(self.output_dir, filename)

            dot = Digraph(comment='Decision Tree', format='png')
            dot.attr(rankdir='TB')
            dot.attr('node', fontname='Meiryo' if self.language == 'ja' else 'Arial')

            def add_node_recursive(node: Dict[str, Any], parent_id: Optional[str] = None):
                node_id = node.get('id', '')
                label = node.get('label', '')
                node_type = node.get('type', 'decision')

                # Set shape based on type
                shape = 'diamond' if node_type == 'decision' else 'box'
                dot.node(node_id, label, shape=shape)

                if parent_id:
                    edge_label = node.get('condition', '')
                    dot.edge(parent_id, node_id, label=edge_label)

                # Add children
                for child in node.get('children', []):
                    add_node_recursive(child, node_id)

            add_node_recursive(root)
            dot.render(output_path, cleanup=True)

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: 'graphviz' library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating decision tree: {e}")
            return ""

    def create_data_flow_diagram(
        self,
        processes: List[Dict[str, str]],
        data_stores: List[Dict[str, str]],
        flows: List[Dict[str, str]],
        filename: str = "data_flow"
    ) -> str:
        """
        Create a data flow diagram (DFD).

        Args:
            processes: List of processes
            data_stores: List of data stores
            flows: List of data flows
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            from graphviz import Digraph

            output_path = os.path.join(self.output_dir, filename)

            dot = Digraph(comment='Data Flow Diagram', format='png')
            dot.attr(rankdir='LR')
            dot.attr('node', fontname='Meiryo' if self.language == 'ja' else 'Arial')

            # Add processes (circles)
            for process in processes:
                proc_id = process.get('id', '')
                label = process.get('label', '')
                dot.node(proc_id, label, shape='circle')

            # Add data stores (rectangles with double line)
            for store in data_stores:
                store_id = store.get('id', '')
                label = store.get('label', '')
                dot.node(store_id, label, shape='rectangle', style='filled', fillcolor='lightgray')

            # Add data flows (edges)
            for flow in flows:
                from_node = flow.get('from', '')
                to_node = flow.get('to', '')
                label = flow.get('data', '')

                dot.edge(from_node, to_node, label=label)

            dot.render(output_path, cleanup=True)

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: 'graphviz' library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating data flow diagram: {e}")
            return ""
