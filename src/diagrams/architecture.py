"""
Architecture diagram generation module.

This module provides functionality for creating system and cloud
architecture diagrams using the 'diagrams' library.
"""

import os
from typing import Dict, List, Any, Optional
from pathlib import Path


class ArchitectureDiagram:
    """
    Class for creating architecture diagrams.

    Supports cloud architecture, data space architecture, and microservices
    diagrams using the 'diagrams' library.

    Attributes:
        theme: Theme configuration dictionary
        language: Language code for labels
        output_dir: Directory for saving generated diagrams
    """

    def __init__(
        self,
        theme: Optional[Dict[str, Any]] = None,
        language: str = "ja",
        output_dir: str = "output/diagrams",
        ai_suggestions: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the ArchitectureDiagram generator.

        Args:
            theme: Theme configuration dictionary
            language: Language code ('ja' or 'en')
            output_dir: Output directory for diagrams
            ai_suggestions: Optional AI-suggested parameters
        """
        self.theme = theme or self._get_default_theme()
        self.language = language
        self.output_dir = output_dir
        self.ai_suggestions = ai_suggestions or {}

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def _get_default_theme(self) -> Dict[str, Any]:
        """Get default theme configuration."""
        return {
            'colors': {
                'primary': '#0066CC',
                'secondary': '#004C99',
                'accent': '#FF6600'
            }
        }

    def _get_label(self, key: str, en: str, ja: str) -> str:
        """
        Get localized label.

        Args:
            key: Label key
            en: English text
            ja: Japanese text

        Returns:
            Localized text based on language setting
        """
        return ja if self.language == 'ja' else en

    def create_three_layer_architecture(
        self,
        layers: Dict[str, List[str]],
        filename: str = "dataspace_architecture"
    ) -> str:
        """
        Create a 3-layer data space architecture diagram.

        Args:
            layers: Dictionary with 'application', 'service', 'data' keys
            filename: Output filename (without extension)

        Returns:
            Path to generated diagram image
        """
        try:
            from diagrams import Diagram, Cluster, Edge
            from diagrams.onprem.client import Client
            from diagrams.onprem.compute import Server
            from diagrams.onprem.database import PostgreSQL
            from diagrams.onprem.queue import Kafka

            output_path = os.path.join(self.output_dir, filename)

            # Get localized labels
            title = self._get_label(
                'title',
                'Data Space 3-Layer Architecture',
                'データスペース 3層アーキテクチャ'
            )

            app_label = self._get_label('app_layer', 'Application Layer', 'アプリケーション層')
            svc_label = self._get_label('svc_layer', 'Service Layer', 'サービス層')
            data_label = self._get_label('data_layer', 'Data Layer', 'データ層')

            with Diagram(
                title,
                show=False,
                direction="TB",
                filename=output_path,
                outformat="png"
            ):
                with Cluster(app_label):
                    apps = [Client(name) for name in layers.get('application', [])]

                with Cluster(svc_label):
                    services = [Server(name) for name in layers.get('service', [])]

                with Cluster(data_label):
                    data_stores = []
                    for name in layers.get('data', []):
                        if 'DB' in name or 'Database' in name:
                            data_stores.append(PostgreSQL(name))
                        else:
                            data_stores.append(Server(name))

                # Connect layers
                if apps and services:
                    for app in apps:
                        app >> services[0]

                if services and data_stores:
                    for service in services:
                        for data_store in data_stores:
                            service >> data_store

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: 'diagrams' library not installed: {e}")
            print("Install with: pip install diagrams")
            return ""

        except Exception as e:
            print(f"Error creating architecture diagram: {e}")
            return ""

    def create_data_space_architecture(
        self,
        layers: List[str],
        flows: Optional[List[Dict[str, str]]] = None,
        filename: str = "dataspace_overview"
    ) -> str:
        """
        Create a general data space architecture diagram.

        Args:
            layers: List of layer names
            flows: Optional list of data flow specifications
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        # Use three_layer_architecture as base implementation
        default_layers = {
            'application': ['Application 1', 'Application 2'],
            'service': ['API Gateway', 'Auth Service', 'Data Catalog'],
            'data': ['Metadata DB', 'Data Storage']
        }

        return self.create_three_layer_architecture(
            default_layers,
            filename
        )

    def create_cloud_architecture(
        self,
        components: List[Dict[str, Any]],
        connections: List[Dict[str, str]],
        filename: str = "cloud_architecture"
    ) -> str:
        """
        Create a cloud architecture diagram.

        Args:
            components: List of cloud components
            connections: List of connections between components
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            from diagrams import Diagram, Cluster, Edge
            from diagrams.aws.compute import EC2, Lambda
            from diagrams.aws.database import RDS
            from diagrams.aws.storage import S3
            from diagrams.aws.network import ELB

            output_path = os.path.join(self.output_dir, filename)

            title = self._get_label(
                'cloud_arch',
                'Cloud Architecture',
                'クラウドアーキテクチャ'
            )

            with Diagram(
                title,
                show=False,
                direction="LR",
                filename=output_path,
                outformat="png"
            ):
                # Create components based on type
                component_map = {}

                for comp in components:
                    comp_type = comp.get('type', 'server')
                    comp_name = comp.get('name', 'Component')

                    if comp_type == 'ec2':
                        component_map[comp_name] = EC2(comp_name)
                    elif comp_type == 'lambda':
                        component_map[comp_name] = Lambda(comp_name)
                    elif comp_type == 'rds':
                        component_map[comp_name] = RDS(comp_name)
                    elif comp_type == 's3':
                        component_map[comp_name] = S3(comp_name)
                    elif comp_type == 'elb':
                        component_map[comp_name] = ELB(comp_name)

                # Create connections
                for conn in connections:
                    from_comp = conn.get('from')
                    to_comp = conn.get('to')
                    label = conn.get('label', '')

                    if from_comp in component_map and to_comp in component_map:
                        if label:
                            component_map[from_comp] >> Edge(label=label) >> component_map[to_comp]
                        else:
                            component_map[from_comp] >> component_map[to_comp]

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: 'diagrams' library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating cloud architecture diagram: {e}")
            return ""

    def create_international_interop_diagram(
        self,
        filename: str = "international_interop"
    ) -> str:
        """
        Create international data space interoperability diagram.

        Specialized diagram showing Ouranos (Japan) and Gaia-X (Europe) connectivity.

        Args:
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            from diagrams import Diagram, Cluster, Edge
            from diagrams.onprem.compute import Server
            from diagrams.onprem.database import PostgreSQL
            from diagrams.onprem.network import Internet

            output_path = os.path.join(self.output_dir, filename)

            title = self._get_label(
                'intl_interop',
                'International Data Space Interoperability',
                'データスペース国際相互運用性'
            )

            with Diagram(
                title,
                show=False,
                direction="LR",
                filename=output_path,
                outformat="png"
            ):
                japan_label = self._get_label('japan', 'Japan', '日本')
                europe_label = self._get_label('europe', 'Europe', '欧州')
                ouranos_label = self._get_label('ouranos', 'Ouranos Ecosystem', 'Ouranos エコシステム')
                gaiax_label = self._get_label('gaiax', 'Gaia-X Framework', 'Gaia-X フレームワーク')

                with Cluster(japan_label):
                    with Cluster(ouranos_label):
                        ouranos_connector = Server("Connector")
                        ouranos_catalog = Server("Catalog")
                        ouranos_data = PostgreSQL("Data")
                        ouranos_connector >> ouranos_catalog
                        ouranos_catalog >> ouranos_data

                with Cluster(europe_label):
                    with Cluster(gaiax_label):
                        gaiax_connector = Server("Connector")
                        gaiax_catalog = Server("Catalog")
                        gaiax_data = PostgreSQL("Data")
                        gaiax_connector >> gaiax_catalog
                        gaiax_catalog >> gaiax_data

                # Interoperability layer
                interop_label = self._get_label(
                    'interop',
                    'Interoperability Layer\n(Standard Protocols)',
                    '相互運用層\n(標準プロトコル)'
                )
                interop = Internet(interop_label)

                ouranos_connector >> Edge(label="API") >> interop
                interop >> Edge(label="API") >> gaiax_connector

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: Required library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating interoperability diagram: {e}")
            return ""

    def create_microservices(
        self,
        services: List[Dict[str, Any]],
        dependencies: List[Dict[str, str]],
        filename: str = "microservices"
    ) -> str:
        """
        Create microservices architecture diagram.

        Args:
            services: List of microservices
            dependencies: List of service dependencies
            filename: Output filename

        Returns:
            Path to generated diagram
        """
        try:
            from diagrams import Diagram, Cluster, Edge
            from diagrams.onprem.compute import Server
            from diagrams.onprem.queue import Kafka
            from diagrams.onprem.database import MongoDB

            output_path = os.path.join(self.output_dir, filename)

            title = self._get_label(
                'microservices',
                'Microservices Architecture',
                'マイクロサービスアーキテクチャ'
            )

            with Diagram(
                title,
                show=False,
                direction="LR",
                filename=output_path,
                outformat="png"
            ):
                service_map = {}

                for svc in services:
                    svc_name = svc.get('name', 'Service')
                    service_map[svc_name] = Server(svc_name)

                # Add message queue if specified
                if any(dep.get('type') == 'async' for dep in dependencies):
                    queue_label = self._get_label('queue', 'Message Queue', 'メッセージキュー')
                    mq = Kafka(queue_label)

                # Create dependencies
                for dep in dependencies:
                    from_svc = dep.get('from')
                    to_svc = dep.get('to')
                    dep_type = dep.get('type', 'sync')

                    if from_svc in service_map and to_svc in service_map:
                        label = 'async' if dep_type == 'async' else 'sync'
                        service_map[from_svc] >> Edge(label=label) >> service_map[to_svc]

            return output_path + ".png"

        except ImportError as e:
            print(f"Error: Required library not installed: {e}")
            return ""

        except Exception as e:
            print(f"Error creating microservices diagram: {e}")
            return ""
