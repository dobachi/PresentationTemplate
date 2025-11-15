# トラブルシューティング

[English](TROUBLESHOOTING.en.md) | 日本語

## Graphvizエラー

### エラー: "Graphviz executable not found"

**原因:** Graphvizのシステムソフトウェアがインストールされていません。

**解決方法:**

Pythonの`graphviz`パッケージとは別に、Graphvizソフトウェアをシステムにインストールする必要があります。

#### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install graphviz
```

#### macOS

```bash
brew install graphviz
```

#### Windows

1. https://graphviz.org/download/ からインストーラーをダウンロード
2. インストール時に「Add to PATH」オプションを選択
3. コマンドプロンプトを再起動

#### インストール確認

```bash
dot -V
```

以下のような出力が表示されればOK:
```
dot - graphviz version 2.x.x
```

### エラー: "'graphviz' Python library not installed"

**原因:** Pythonのgraphvizパッケージがインストールされていません。

**解決方法:**

```bash
# uvを使用している場合
uv pip install graphviz

# pipを使用している場合
pip install graphviz
```

## 依存関係のエラー

### エラー: "No module named 'diagrams'"

**解決方法:**

```bash
# 全依存関係の再インストール
uv pip install -r requirements.txt

# または
pip install -r requirements.txt
```

### エラー: "No module named 'matplotlib'"

matplotlibでフォントに関するエラーが出る場合:

**Ubuntu/Debian:**
```bash
sudo apt-get install fonts-noto-cjk  # 日本語フォント
```

**macOS:**
```bash
brew install font-noto-sans-cjk-jp
```

## PowerPoint生成エラー

### エラー: "Permission denied" when saving .pptx

**原因:** 出力ディレクトリに書き込み権限がありません。

**解決方法:**

```bash
# outputディレクトリの作成と権限設定
mkdir -p output
chmod 755 output
```

### エラー: 日本語フォントが文字化けする

**解決方法:**

```python
# Meiryoフォントが利用可能か確認
from src.i18n import FontSelector

selector = FontSelector()
fonts = selector.get_all_fonts_for_language('ja')
print(fonts)
```

システムに日本語フォントがインストールされていることを確認してください。

## パフォーマンスの問題

### 図表生成が遅い

**解決方法:**

1. **uvを使用** - pip より高速:
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

2. **出力解像度を調整** - 必要に応じてDPIを下げる:
   ```python
   chart.create_line_chart(..., dpi=150)  # デフォルトは300
   ```

## よくある質問

### Q: フローチャートが生成されない

A: Graphvizのシステムインストールを確認してください:
```bash
which dot  # Linux/macOS
where dot  # Windows
```

### Q: 図表の日本語が表示されない

A: 以下を確認:
1. システムに日本語フォントがインストールされている
2. `language='ja'`パラメータが設定されている
3. Meiryoまたは代替フォントが利用可能

### Q: 仮想環境が有効化できない

A: OSに応じた正しいコマンドを使用:

**Linux/macOS:**
```bash
source .venv/bin/activate  # uv
source venv/bin/activate   # venv
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1  # uv
venv\Scripts\Activate.ps1   # venv
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat  # uv
venv\Scripts\activate.bat   # venv
```

## サポート

問題が解決しない場合:

1. [Issues](https://github.com/dobachi/PresentationTemplate/issues) で既存の問題を検索
2. 新しいIssueを作成（エラーメッセージ全体を含める）
3. 以下の情報を含める:
   - OS名とバージョン
   - Pythonバージョン (`python --version`)
   - インストール方法（uv/pip）
   - エラーメッセージ全体

## 関連リンク

- [README](README.md) - インストール手順
- [Graphviz公式サイト](https://graphviz.org/)
- [python-pptx ドキュメント](https://python-pptx.readthedocs.io/)
