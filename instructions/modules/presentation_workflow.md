# プレゼンテーション生成ワークフロー

## 完全な作業フロー

### Phase 1: 要件定義（5-10分）
1. ユーザーとの対話で情報収集
2. 要件YAMLの生成
3. ユーザー確認

### Phase 2: コンテンツ設計（10-15分）
1. スライド構成の提案
2. 各スライドの図表選定
3. フィードバック反映

### Phase 3: 図表生成（自動）
1. 必要な図表をすべて生成
2. 画像ファイルとして保存
3. サイズ・品質の確認

### Phase 4: PowerPoint生成（自動）
1. テンプレート読み込み
2. スライド作成
3. 図表配置
4. テキスト挿入

### Phase 5: レビュー（5-10分）
1. プレビュー提示
2. 修正要望の受付
3. 再生成

## チェックポイント統合

AI_Instruction_Kitsのチェックポイントシステムを使用：

```bash
# タスク開始
checkpoint.sh start "プレゼンテーション作成: データスペース相互運用性"

# 進捗報告
checkpoint.sh progress TASK-001 1 4 "要件定義完了"
checkpoint.sh progress TASK-001 2 4 "スライド構成決定"
checkpoint.sh progress TASK-001 3 4 "図表生成完了"
checkpoint.sh progress TASK-001 4 4 "PowerPoint生成完了"

# タスク完了
checkpoint.sh complete TASK-001 "プレゼンテーション完成"
```

## 使用例: データスペース相互運用性プレゼン作成

### ステップ1: 初期対話
```
ユーザー: 「データスペースの国際相互運用性について15分のプレゼンを作りたい」

AI: 「承知しました。以下の点について教えてください：
1. 対象は技術者ですか、それともビジネス向けですか？
2. 特に強調したい要素は何ですか？（例：セキュリティ、相互運用性、ガバナンス）
3. 具体的な事例を含めますか？
4. 言語は日本語、英語、それとも両方ですか？」

ユーザー: 「技術者向けで、特に相互運用性を強調。日欧の事例（OuranosとGaia-X）を含めて。日本語で」

AI: 「理解しました。以下の構成を提案します：」
```

### ステップ2: 構成提案
```yaml
presentation:
  title: "データスペース国際相互運用性"
  subtitle: "日欧連携の現状と展望"
  author: "Dobachi"
  duration: 15
  language: "ja"
  theme: "corporate"

slides:
  - type: title
    title: "データスペース国際相互運用性"
    subtitle: "日欧連携の現状と展望"

  - type: content
    title: "データスペースとは"
    layout: "diagram"
    content:
      diagram_type: "architecture"
      diagram_spec: "3層アーキテクチャ"
    notes: "データ層、サービス層、アプリケーション層の概念を説明"

  - type: content
    title: "相互運用性の課題"
    layout: "text_with_diagram"
    bullets:
      - "技術的標準の統一"
      - "ガバナンスの調和"
      - "データ主権の尊重"
    content:
      diagram_type: "flowchart"
      diagram_spec: "課題フロー"

  - type: content
    title: "Ouranos エコシステム（日本）"
    layout: "diagram"
    content:
      diagram_type: "architecture"
      diagram_spec: "Ouranosアーキテクチャ"
    notes: "日本のデータスペース実装"

  - type: content
    title: "Gaia-X フレームワーク（欧州）"
    layout: "diagram"
    content:
      diagram_type: "architecture"
      diagram_spec: "Gaia-Xアーキテクチャ"
    notes: "欧州のデータスペース実装"

  - type: content
    title: "国際相互運用性モデル"
    layout: "diagram"
    content:
      diagram_type: "network"
      diagram_spec: "日欧接続図"
    notes: "Ouranos ↔ Gaia-X 相互運用"

  - type: content
    title: "標準プロトコルマッピング"
    layout: "chart"
    content:
      chart_type: "comparison_table"
      data:
        - ["項目", "Ouranos", "Gaia-X", "共通標準"]
        - ["認証", "OAuth 2.0", "OAuth 2.0", "○"]
        - ["データ形式", "JSON-LD", "JSON-LD", "○"]
        - ["メタデータ", "DCAT-AP JP", "DCAT-AP", "△"]

  - type: content
    title: "採用トレンド"
    layout: "chart"
    content:
      chart_type: "line"
      data:
        x: [2020, 2021, 2022, 2023, 2024]
        y_ouranos: [10, 25, 45, 80, 120]
        y_gaiax: [30, 60, 95, 140, 200]

  - type: content
    title: "まとめ"
    layout: "text"
    bullets:
      - "日欧データスペースの相互運用性は着実に進展"
      - "標準プロトコルの統一が重要"
      - "今後の課題：ガバナンス調和、データ主権"
      - "継続的な対話と技術協力が必要"
```

### ステップ3: フィードバックと改善
```
ユーザー: 「3層アーキテクチャの図を詳しく作って」

AI: 「承知しました。3層構造のアーキテクチャ図を詳細に作成します：

- データ層（下層）：メタデータDB、データストレージ、オブジェクトストア
- サービス層（中層）：API Gateway、認証サービス、データカタログ
- アプリケーション層（上層）：各種アプリケーション

それぞれの接続とデータフローを示します。色はcorporateテーマ（青系）でよろしいですか？」

ユーザー: 「OK、それで進めて」
```

### ステップ4: 実装（自動実行）
```python
# AI が実行するコード
from presentation_generator import PresentationBuilder
from presentation_generator.diagrams import ArchitectureDiagram
from presentation_generator.charts import StatisticalChart

# ビルダー初期化
builder = PresentationBuilder(theme='corporate', language='ja')

# タイトルスライド
builder.add_title_slide(
    title="データスペース国際相互運用性",
    subtitle="日欧連携の現状と展望"
)

# 3層アーキテクチャ図生成
arch_diagram = ArchitectureDiagram(theme='corporate', language='ja')
diagram_path = arch_diagram.create_three_layer_architecture(
    layers={
        'application': ['App 1', 'App 2', 'App 3'],
        'service': ['API Gateway', '認証サービス', 'データカタログ'],
        'data': ['メタデータDB', 'データストレージ', 'オブジェクトストア']
    }
)
builder.add_diagram_slide(
    title="データスペースとは",
    diagram_path=diagram_path
)

# ... 他のスライドも同様に生成

# 保存
builder.save('データスペース相互運用性.pptx')
```

### ステップ5: 完成と配信
```
AI: 「プレゼンテーションが完成しました！

📊 生成内容:
- スライド数: 9枚
- 図表数: 5個（アーキテクチャ図×3、ネットワーク図×1、折れ線グラフ×1）
- ファイルサイズ: 2.3MB
- 形式: PowerPoint (.pptx)

ファイルをダウンロード: データスペース相互運用性.pptx

修正が必要な箇所があれば教えてください。」
```

## バイリンガル対応

### 日本語プレゼンテーション
```python
builder = PresentationBuilder(theme='corporate', language='ja')
builder.set_fonts(
    title_font='Meiryo',
    body_font='Meiryo',
    code_font='Consolas'
)
```

### 英語プレゼンテーション
```python
builder = PresentationBuilder(theme='corporate', language='en')
builder.set_fonts(
    title_font='Arial',
    body_font='Arial',
    code_font='Courier New'
)
```

### 日英混在プレゼンテーション
```python
builder = PresentationBuilder(theme='corporate', language='ja_en')
builder.set_fonts(
    title_font='Meiryo',  # 日本語サポート
    body_font='Arial',    # 英語最適
    code_font='Consolas'
)

# スライドごとに言語指定可能
builder.add_title_slide(
    title="Data Space Architecture",
    subtitle="データスペースアーキテクチャ"
)
```

## エラーハンドリングと代替案

### 図表生成失敗時
```python
try:
    diagram_path = arch_diagram.create_architecture(...)
except Exception as e:
    # フォールバック: テキストベースの説明
    builder.add_text_slide(
        title="システムアーキテクチャ",
        bullets=[
            "アプリケーション層: ユーザー向けアプリケーション",
            "サービス層: API、認証、カタログサービス",
            "データ層: データベース、ストレージ"
        ]
    )
    print(f"Warning: Diagram generation failed, using text fallback. Error: {e}")
```

### ライブラリ未インストール時
```python
try:
    from diagrams import Diagram
except ImportError:
    print("Warning: 'diagrams' library not installed")
    print("Suggestion: pip install diagrams")
    print("Alternative: Using graphviz for simpler diagrams")
```

## パフォーマンス最適化

### 並列図表生成
```python
from concurrent.futures import ThreadPoolExecutor

diagrams_to_generate = [
    ('architecture_3layer', arch_diagram.create_three_layer_architecture, {...}),
    ('ouranos', arch_diagram.create_ouranos_architecture, {...}),
    ('gaiax', arch_diagram.create_gaiax_architecture, {...}),
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(func, **kwargs): name
               for name, func, kwargs in diagrams_to_generate}

    for future in futures:
        diagram_name = futures[future]
        diagram_path = future.result()
        print(f"Generated: {diagram_name} -> {diagram_path}")
```

### キャッシング
```python
import hashlib
import pickle

def cached_diagram(func):
    def wrapper(*args, **kwargs):
        # 引数からキャッシュキー生成
        cache_key = hashlib.md5(
            pickle.dumps((args, kwargs))
        ).hexdigest()

        cache_file = f".cache/diagram_{cache_key}.png"

        if os.path.exists(cache_file):
            print(f"Using cached diagram: {cache_file}")
            return cache_file

        # 生成して保存
        result = func(*args, **kwargs)
        os.makedirs('.cache', exist_ok=True)
        shutil.copy(result, cache_file)
        return result

    return wrapper

@cached_diagram
def create_architecture(...):
    # ...
```

## ライセンス
MIT License - Based on AI_Instruction_Kits framework
