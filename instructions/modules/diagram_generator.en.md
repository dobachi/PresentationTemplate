# Diagram Generation AI

## Role
Provide instructions for generating technical diagrams using appropriate libraries.

## Diagram Types and Libraries

### Architecture Diagrams → diagrams library
```python
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3

with Diagram("Data Space Architecture", show=False, direction="TB"):
    with Cluster("Application Layer"):
        app = EC2("App Server")
    with Cluster("Data Layer"):
        db = RDS("Database")
        storage = S3("Object Storage")

    app >> Edge(label="query") >> db
    app >> Edge(label="store") >> storage
```

**Available Providers:**
- `diagrams.aws.*` - AWS services
- `diagrams.azure.*` - Azure services
- `diagrams.gcp.*` - GCP services
- `diagrams.k8s.*` - Kubernetes components
- `diagrams.onprem.*` - On-premise (generic servers, DB, etc.)
- `diagrams.programming.*` - Programming languages/frameworks

### Flow Diagrams → graphviz
```python
from graphviz import Digraph

dot = Digraph(comment='Process Flow', format='png')
dot.attr(rankdir='TB', size='8,6')

# Node definitions
dot.node('A', 'Start', shape='ellipse')
dot.node('B', 'Authentication', shape='box')
dot.node('C', 'Data Processing', shape='box')
dot.node('D', 'End', shape='ellipse')

# Edge definitions
dot.edge('A', 'B', label='Request')
dot.edge('B', 'C', label='Auth Success')
dot.edge('C', 'D', label='Complete')

dot.render('flowchart', cleanup=True)
```

**Shape Options:**
- `ellipse` - Start/End
- `box` - Process
- `diamond` - Decision
- `parallelogram` - Input/Output

### Network Diagrams → networkx + matplotlib
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes (countries/regions)
G.add_node("Japan", type="region")
G.add_node("Europe", type="region")
G.add_node("Ouranos", type="dataspace")
G.add_node("Gaia-X", type="dataspace")

# Add edges (connections)
G.add_edge("Japan", "Ouranos", weight=5)
G.add_edge("Europe", "Gaia-X", weight=5)
G.add_edge("Ouranos", "Gaia-X", weight=3, label="Interoperability")

# Draw
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=3000, font_size=10, font_weight='bold')
plt.savefig('network.png', dpi=300, bbox_inches='tight')
```

### Statistical Charts → matplotlib/seaborn
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Font settings for English
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Line chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_data, y_data, marker='o', linewidth=2, markersize=8)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)
ax.set_title('Data Space Adoption Trend', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
```

## Data Space Specialized Diagram Templates

Diagrams specialized for Dobachi's work:

### 1. Data Space 3-Layer Architecture
```python
from diagrams import Diagram, Cluster
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

with Diagram("Data Space 3-Layer Architecture",
             show=False,
             direction="TB",
             filename="dataspace_architecture"):

    with Cluster("Application Layer"):
        apps = [Client("App 1"), Client("App 2"), Client("App 3")]

    with Cluster("Service Layer"):
        services = [Server("API Gateway"),
                   Server("Auth Service"),
                   Server("Data Catalog")]

    with Cluster("Data Layer"):
        data = [PostgreSQL("Metadata DB"),
                Server("Data Storage"),
                Server("Object Store")]

    # Define connections
    for app in apps:
        app >> services[0]

    services[0] >> services[1]
    services[0] >> services[2]

    for service in services:
        for d in data:
            service >> d
```

### 2. International Data Space Interoperability Diagram
```python
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet

with Diagram("International Data Space Interoperability",
             show=False,
             direction="LR",
             filename="international_interop"):

    with Cluster("Japan"):
        with Cluster("Ouranos Ecosystem"):
            ouranos_connector = Server("Connector")
            ouranos_catalog = Server("Catalog")
            ouranos_data = PostgreSQL("Data")

    with Cluster("Europe"):
        with Cluster("Gaia-X Framework"):
            gaiax_connector = Server("Connector")
            gaiax_catalog = Server("Catalog")
            gaiax_data = PostgreSQL("Data")

    # Interoperability layer
    interop = Internet("Interoperability Layer\n(Standard Protocols)")

    ouranos_connector >> Edge(label="API") >> interop
    interop >> Edge(label="API") >> gaiax_connector
```

### 3. Data Space High-Level Architecture Model (DS-HLAM)
```python
from diagrams import Diagram, Cluster
from diagrams.programming.framework import React
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB

with Diagram("DS-HLAM Architecture Model",
             show=False,
             direction="TB",
             filename="ds_hlam"):

    with Cluster("Governance"):
        gov = Server("Policy Manager")

    with Cluster("Orchestration"):
        orch = [Server("Workflow Engine"), Server("Service Registry")]

    with Cluster("Data Exchange"):
        exchange = [Server("Data Connector"), Server("Protocol Adapter")]

    with Cluster("Trust & Security"):
        trust = [Server("Identity Provider"), Server("Access Control")]

    # Hierarchical connections
    gov >> orch[0]
    orch[0] >> exchange[0]
    orch[1] >> exchange[1]
    trust[0] >> orch[0]
    trust[1] >> exchange[0]
```

## Multi-language Support

### Font Settings for Japanese Presentations
```python
import matplotlib.pyplot as plt

# Japanese font settings
plt.rcParams['font.sans-serif'] = ['Meiryo', 'Hiragino Sans', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# Japanese titles and labels available
plt.title('データスペース採用率の推移', fontsize=14)
plt.xlabel('年度', fontsize=12)
plt.ylabel('採用率 (%)', fontsize=12)
```

### Font Settings for English Presentations
```python
import matplotlib.pyplot as plt

# English font settings
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'

# English labels
plt.title('Data Space Adoption Trend', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (%)', fontsize=12)
```

## Image Quality Settings

All diagrams generated in high quality:

```python
# DPI settings (300 DPI recommended for presentations)
plt.savefig('output.png', dpi=300, bbox_inches='tight', facecolor='white')

# For transparent background if needed
plt.savefig('output.png', dpi=300, bbox_inches='tight', transparent=True)
```

## Error Handling

```python
try:
    # Diagram generation code
    with Diagram("Example", show=False):
        # ...
except ImportError as e:
    print(f"Warning: Required library not installed: {e}")
    print("Suggestion: Use alternative diagram type")
except Exception as e:
    print(f"Error generating diagram: {e}")
    print("Fallback: Create text-based representation")
```

## License
MIT License - Based on AI_Instruction_Kits framework
