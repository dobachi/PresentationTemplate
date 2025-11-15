# 図表生成AI

## 役割
技術図表を適切なライブラリを使って生成する指示を提供します。

## 図表タイプと使用ライブラリ

### アーキテクチャ図 → diagrams library
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

**利用可能なプロバイダー:**
- `diagrams.aws.*` - AWS サービス
- `diagrams.azure.*` - Azure サービス
- `diagrams.gcp.*` - GCP サービス
- `diagrams.k8s.*` - Kubernetes コンポーネント
- `diagrams.onprem.*` - オンプレミス（汎用サーバー、DB等）
- `diagrams.programming.*` - プログラミング言語/フレームワーク

### フロー図 → graphviz
```python
from graphviz import Digraph

dot = Digraph(comment='Process Flow', format='png')
dot.attr(rankdir='TB', size='8,6')

# ノード定義
dot.node('A', '開始', shape='ellipse')
dot.node('B', '認証', shape='box')
dot.node('C', 'データ処理', shape='box')
dot.node('D', '終了', shape='ellipse')

# エッジ定義
dot.edge('A', 'B', label='リクエスト')
dot.edge('B', 'C', label='認証成功')
dot.edge('C', 'D', label='完了')

dot.render('flowchart', cleanup=True)
```

**形状オプション:**
- `ellipse` - 開始/終了
- `box` - プロセス
- `diamond` - 判断
- `parallelogram` - 入出力

### ネットワーク図 → networkx + matplotlib
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# ノード追加（国・地域）
G.add_node("Japan", type="region")
G.add_node("Europe", type="region")
G.add_node("Ouranos", type="dataspace")
G.add_node("Gaia-X", type="dataspace")

# エッジ追加（接続関係）
G.add_edge("Japan", "Ouranos", weight=5)
G.add_edge("Europe", "Gaia-X", weight=5)
G.add_edge("Ouranos", "Gaia-X", weight=3, label="Interoperability")

# 描画
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=3000, font_size=10, font_weight='bold')
plt.savefig('network.png', dpi=300, bbox_inches='tight')
```

### 統計グラフ → matplotlib/seaborn
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 日本語フォント設定
plt.rcParams['font.sans-serif'] = ['Meiryo', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 折れ線グラフ
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_data, y_data, marker='o', linewidth=2, markersize=8)
ax.set_xlabel('年度', fontsize=12)
ax.set_ylabel('採用率 (%)', fontsize=12)
ax.set_title('データスペース採用推移', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
```

## データスペース専用図表テンプレート

Dobachiさんの業務に特化した図表：

### 1. データスペース3層アーキテクチャ
```python
from diagrams import Diagram, Cluster
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

with Diagram("Data Space 3-Layer Architecture",
             show=False,
             direction="TB",
             filename="dataspace_architecture"):

    with Cluster("Application Layer (アプリケーション層)"):
        apps = [Client("App 1"), Client("App 2"), Client("App 3")]

    with Cluster("Service Layer (サービス層)"):
        services = [Server("API Gateway"),
                   Server("Auth Service"),
                   Server("Data Catalog")]

    with Cluster("Data Layer (データ層)"):
        data = [PostgreSQL("Metadata DB"),
                Server("Data Storage"),
                Server("Object Store")]

    # 接続定義
    for app in apps:
        app >> services[0]

    services[0] >> services[1]
    services[0] >> services[2]

    for service in services:
        for d in data:
            service >> d
```

### 2. 国際データスペース相互運用性図
```python
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet

with Diagram("International Data Space Interoperability",
             show=False,
             direction="LR",
             filename="international_interop"):

    with Cluster("Japan (日本)"):
        with Cluster("Ouranos Ecosystem"):
            ouranos_connector = Server("Connector")
            ouranos_catalog = Server("Catalog")
            ouranos_data = PostgreSQL("Data")

    with Cluster("Europe (欧州)"):
        with Cluster("Gaia-X Framework"):
            gaiax_connector = Server("Connector")
            gaiax_catalog = Server("Catalog")
            gaiax_data = PostgreSQL("Data")

    # 相互運用性レイヤー
    interop = Internet("Interoperability Layer\n(標準プロトコル)")

    ouranos_connector >> Edge(label="API") >> interop
    interop >> Edge(label="API") >> gaiax_connector
```

### 3. データスペース高レベルアーキテクチャモデル (DS-HLAM)
```python
from diagrams import Diagram, Cluster
from diagrams.programming.framework import React
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB

with Diagram("DS-HLAM Architecture Model",
             show=False,
             direction="TB",
             filename="ds_hlam"):

    with Cluster("Governance (ガバナンス)"):
        gov = Server("Policy Manager")

    with Cluster("Orchestration (オーケストレーション)"):
        orch = [Server("Workflow Engine"), Server("Service Registry")]

    with Cluster("Data Exchange (データ交換)"):
        exchange = [Server("Data Connector"), Server("Protocol Adapter")]

    with Cluster("Trust & Security (信頼・セキュリティ)"):
        trust = [Server("Identity Provider"), Server("Access Control")]

    # 階層的な接続
    gov >> orch[0]
    orch[0] >> exchange[0]
    orch[1] >> exchange[1]
    trust[0] >> orch[0]
    trust[1] >> exchange[0]
```

## 多言語対応

### 日本語プレゼンテーション用フォント設定
```python
import matplotlib.pyplot as plt

# 日本語フォント設定
plt.rcParams['font.sans-serif'] = ['Meiryo', 'Hiragino Sans', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# 図表タイトルやラベルに日本語を使用可能
plt.title('データスペース採用率の推移', fontsize=14)
plt.xlabel('年度', fontsize=12)
plt.ylabel('採用率 (%)', fontsize=12)
```

### 英語プレゼンテーション用フォント設定
```python
import matplotlib.pyplot as plt

# 英語フォント設定
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'

# English labels
plt.title('Data Space Adoption Trend', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (%)', fontsize=12)
```

## 画像品質設定

すべての図表は高品質で生成：

```python
# DPI設定（プレゼンテーション用は300 DPI推奨）
plt.savefig('output.png', dpi=300, bbox_inches='tight', facecolor='white')

# 透過背景が必要な場合
plt.savefig('output.png', dpi=300, bbox_inches='tight', transparent=True)
```

## エラーハンドリング

```python
try:
    # 図表生成コード
    with Diagram("Example", show=False):
        # ...
except ImportError as e:
    print(f"Warning: Required library not installed: {e}")
    print("Suggestion: Use alternative diagram type")
except Exception as e:
    print(f"Error generating diagram: {e}")
    print("Fallback: Create text-based representation")
```

## ライセンス
MIT License - Based on AI_Instruction_Kits framework
