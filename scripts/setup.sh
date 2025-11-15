#!/bin/bash
# PresentationTemplate セットアップスクリプト
# 仮想環境の作成と依存関係のインストールをワンライナーで実行

set -e  # エラーで停止

echo "=========================================="
echo "PresentationTemplate セットアップ"
echo "=========================================="
echo

# uvがインストールされているか確認
if command -v uv &> /dev/null; then
    echo "✓ uv が見つかりました"
    USE_UV=true
else
    echo "⚠️  uv が見つかりません。pipを使用します。"
    echo "   uvのインストール: curl -LsSf https://astral.sh/uv/install.sh | sh"
    USE_UV=false
fi

echo

# 仮想環境作成
if [ "$USE_UV" = true ]; then
    echo "→ uvで仮想環境を作成中..."
    uv venv
    VENV_PYTHON=".venv/bin/python"
else
    echo "→ venvで仮想環境を作成中..."
    python3 -m venv venv
    VENV_PYTHON="venv/bin/python"
fi

echo "✓ 仮想環境作成完了"
echo

# 依存関係インストール
echo "→ 依存関係をインストール中..."
if [ "$USE_UV" = true ]; then
    uv pip install -e .
else
    $VENV_PYTHON -m pip install --upgrade pip
    $VENV_PYTHON -m pip install -e .
fi

echo "✓ 依存関係インストール完了"
echo

# 依存関係チェック
echo "→ インストール確認中..."
$VENV_PYTHON scripts/check_dependencies.py

echo
echo "=========================================="
echo "セットアップ完了！"
echo "=========================================="
echo
echo "次のステップ:"
echo

if [ "$USE_UV" = true ]; then
    echo "  仮想環境を有効化:"
    echo "    source .venv/bin/activate"
    echo
    echo "  または仮想環境のPythonを直接使用:"
    echo "    .venv/bin/python examples/architecture_example.py"
else
    echo "  仮想環境を有効化:"
    echo "    source venv/bin/activate"
    echo
    echo "  または仮想環境のPythonを直接使用:"
    echo "    venv/bin/python examples/architecture_example.py"
fi

echo
