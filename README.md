# AI支援グラフィカルプレゼンテーション生成システム

[English](README.en.md) | 日本語

**AI_Instruction_Kits**と連携して、技術・ビジネスコンテンツ向けの専門的でグラフィカルなプレゼンテーションをAI支援で作成するPythonベースのプレゼンテーション生成フレームワーク。

## 機能

- **AI支援会話モード**: 自然言語での対話を通じてプレゼンテーションを作成
- **多様な図表タイプ**: `diagrams`、`graphviz`、`networkx`を使用したアーキテクチャ図、フローチャート、ネットワーク図
- **統計グラフ**: `matplotlib`と`seaborn`を使用した折れ線グラフ、棒グラフ、散布図、円グラフ
- **バイリンガル対応**: 適切なフォント処理による日本語・英語のプレゼンテーション
- **テーマシステム**: Corporate、Technical、Academicテーマ
- **PowerPoint生成**: `python-pptx`による専門的な.pptxファイル

## インストール

### 前提条件

- Python 3.8以上
- Graphviz（フローチャート用）
- [uv](https://github.com/astral-sh/uv) - 高速なPythonパッケージインストーラー（推奨）

### uvのインストール（推奨）

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**代替方法（pipを使用）:**
```bash
pip install uv
```

### Graphvizのインストール

**Ubuntu/Debian:**
```bash
sudo apt-get install graphviz
```

**macOS:**
```bash
brew install graphviz
```

**Windows:**
https://graphviz.org/download/ からダウンロード

### パッケージのインストール

#### クイックセットアップ（推奨）

**ワンライナーで自動セットアップ:**

```bash
bash scripts/setup.sh
```

このスクリプトが自動的に実行：
- uvまたはpipの検出
- 仮想環境の作成
- 依存関係のインストール
- インストール確認

#### 手動セットアップ

##### オプション1: uvを使用（推奨 - 高速）

```bash
# リポジトリのクローン
git clone https://github.com/dobachi/PresentationTemplate.git
cd PresentationTemplate

# AI_Instruction_Kitsサブモジュールの初期化
git submodule update --init --recursive

# 仮想環境の作成
uv venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows

# 依存関係のインストール（pyproject.tomlから自動読み込み）
uv pip install -e .
```

##### オプション2: 従来のvenv + pipを使用

```bash
# リポジトリのクローン
git clone https://github.com/dobachi/PresentationTemplate.git
cd PresentationTemplate

# AI_Instruction_Kitsサブモジュールの初期化
git submodule update --init --recursive

# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows

# 依存関係のインストール（pyproject.tomlから自動読み込み）
pip install -e .
```

## クイックスタート

### 方法1: AI支援モード（推奨）

CLAUDE.mdファイルを使ってClaudeと直接対話：

```
データスペース国際相互運用性について15分のプレゼンを作りたい。
日欧協力（OuranosとGaia-X）に焦点を当てて。
対象者は技術者、言語は日本語。
```

Claudeが以下を実行：
1. 確認質問
2. スライド構成の提案
3. 図表の自動生成
4. PowerPointファイルの作成

### 方法2: Python API

```python
from src.core.presentation import PresentationBuilder
from src.diagrams.architecture import ArchitectureDiagram
from src.charts.statistical import StatisticalChart

# ビルダーの作成
builder = PresentationBuilder(theme='corporate', language='ja')

# タイトルスライドの追加
builder.add_title_slide(
    title="データスペース国際相互運用性",
    subtitle="日欧協力"
)

# アーキテクチャ図の生成と追加
arch_diagram = ArchitectureDiagram(language='ja')
diagram_path = arch_diagram.create_three_layer_architecture(
    layers={
        'application': ['アプリ1', 'アプリ2', 'アプリ3'],
        'service': ['APIゲートウェイ', '認証サービス', 'データカタログ'],
        'data': ['メタデータDB', 'データストレージ', 'オブジェクトストア']
    }
)
builder.add_diagram_slide(
    title="データスペース3層アーキテクチャ",
    diagram_path=diagram_path
)

# グラフの生成と追加
chart = StatisticalChart(language='ja')
chart_path = chart.create_line_chart(
    data={
        'x': [2020, 2021, 2022, 2023, 2024],
        'y_ouranos': [10, 25, 45, 80, 120],
        'y_gaiax': [30, 60, 95, 140, 200]
    },
    labels={
        'x_axis': '年度',
        'y_axis': '採用率',
        'y_ouranos': 'Ouranos',
        'y_gaiax': 'Gaia-X'
    },
    title='データスペース採用トレンド'
)
builder.add_chart_slide(
    title="採用トレンド",
    chart_path=chart_path
)

# プレゼンテーションの保存
builder.save('output/DataSpace_Interoperability.pptx')
```

### 方法3: YAML定義

YAMLファイルの作成：

```yaml
presentation:
  title: "データスペースアーキテクチャ"
  author: "Dobachi"
  language: "ja"
  theme: "corporate"

slides:
  - type: title
    title: "データスペースアーキテクチャ"
    subtitle: "概要とコンポーネント"

  - type: content
    title: "イントロダクション"
    layout: "text"
    bullets:
      - "データスペースとは"
      - "なぜ重要か"
      - "主要コンポーネント"
```

生成：

```python
builder = PresentationBuilder()
builder.load_definition('my_presentation.yaml')
builder.build_from_definition(builder.load_definition('my_presentation.yaml'))
builder.save('output.pptx')
```

## サポートする図表タイプ

### アーキテクチャ図

- 3層アーキテクチャ（データ/サービス/アプリケーション）
- クラウドアーキテクチャ（AWS、Azure、GCP）
- マイクロサービスアーキテクチャ
- 国際相互運用性（Ouranos ↔ Gaia-X）

### フローチャート

- プロセスフロー
- 決定木
- データフロー図

### ネットワーク図

- ネットワークトポロジー
- 相互運用性ネットワーク
- 接続図

### 統計グラフ

- 折れ線グラフ
- 棒グラフ（縦/横）
- 散布図
- 円グラフ
- 積み上げ棒グラフ

## バイリンガル対応

### 日本語プレゼンテーション

```python
builder = PresentationBuilder(theme='corporate', language='ja')
builder.set_fonts(
    title_font='Meiryo',
    body_font='Meiryo'
)
```

### 英語プレゼンテーション

```python
builder = PresentationBuilder(theme='corporate', language='en')
builder.set_fonts(
    title_font='Arial',
    body_font='Arial'
)
```

### 日英混在

```python
builder = PresentationBuilder(theme='corporate', language='ja_en')
builder.add_title_slide(
    title="Data Space Architecture",
    subtitle="データスペースアーキテクチャ"
)
```

## テーマ

3つの組み込みテーマ：

- **Corporate**: プロフェッショナルな青系テーマ
- **Technical**: ダークアクセントの技術テーマ
- **Academic**: アカデミックスタイル

カスタムテーマは`config/themes/`で作成可能。

## サンプル

`examples/`ディレクトリを参照：

- `architecture_example.py` - アーキテクチャ図のサンプル
- `full_presentation_example.py` - 完全なプレゼンテーションのサンプル
- `example_conversation.md` - AIとの会話サンプル

## AI指示ファイル

`instructions/modules/`に専門的なAI指示モジュールを含む：

- `presentation_designer.md` - 設計のための会話ガイド
- `diagram_generator.md` - 図表作成指示
- `presentation_workflow.md` - エンドツーエンドのワークフロー

これらは[AI_Instruction_Kits](https://github.com/dobachi/AI_Instruction_Kits)フレームワークと連携します。

## プロジェクト構造

```
PresentationTemplate/
├── src/                      # ライブラリコード（変更しない）
│   ├── core/                 # コアプレゼンテーション構築
│   ├── diagrams/             # 図表生成ライブラリ
│   ├── charts/               # グラフ生成ライブラリ
│   ├── i18n/                 # 国際化・フォント選択
│   ├── ai/                   # AI会話フロー
│   └── utils/                # ユーティリティ
├── scripts/                  # ユーザースクリプト（ここに作成）
│   ├── setup.sh              # セットアップスクリプト
│   ├── check_dependencies.py # 依存関係確認
│   └── generate_*.py         # プレゼンテーション生成スクリプト
├── config/
│   └── themes/               # テーマ設定
├── instructions/
│   ├── ai_instruction_kits/  # サブモジュール
│   └── modules/              # カスタム指示モジュール
├── examples/                 # サンプルコード（参考用）
│   ├── architecture_example.py
│   └── full_presentation_example.py
├── output/                   # 生成されたプレゼンテーション
└── templates/                # PowerPointテンプレート
```

### ディレクトリの役割

- **`src/`**: このテンプレートが提供するライブラリコード。**変更しない**
- **`scripts/`**: ユーザーがプレゼンテーション生成用に作成するスクリプト。**ここに作成**
- **`examples/`**: 使い方の参考となるサンプルコード
- **`output/`**: 生成された.pptxファイルが保存される場所

## トラブルシューティング

問題が発生した場合は、[トラブルシューティングガイド](TROUBLESHOOTING.md)を参照してください。

よくある問題：
- **Graphvizエラー**: システムにGraphvizがインストールされていることを確認
- **日本語フォントの問題**: Meiryoまたは代替フォントがインストールされている必要があります
- **依存関係エラー**: `uv pip install -e .` で再インストール

## ライセンス

MIT License

## コントリビューション

コントリビューション歓迎！ガイドラインはCONTRIBUTING.mdを参照してください。

## 作者

Dobachi

## 謝辞

- [AI_Instruction_Kits](https://github.com/dobachi/AI_Instruction_Kits)の上に構築
- [python-pptx](https://python-pptx.readthedocs.io/)を使用
- [diagrams](https://diagrams.mingrammer.com/)による図表生成
