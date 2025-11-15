# Makefile for PresentationTemplate
# プレゼンテーション生成を簡単にするためのMakefile

.PHONY: help setup install clean build test check examples

# デフォルトターゲット
.DEFAULT_GOAL := help

# 仮想環境のPython
VENV_PYTHON := .venv/bin/python
VENV_PIP := .venv/bin/pip

# 出力ディレクトリ
OUTPUT_DIR := output

help: ## ヘルプメッセージを表示
	@echo "利用可能なコマンド:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "使用例:"
	@echo "  make setup              # 初回セットアップ"
	@echo "  make build SCRIPT=scripts/generate_presentation.py"
	@echo "  make examples           # サンプル実行"

setup: ## 初回セットアップ（仮想環境作成と依存関係インストール）
	@echo "→ セットアップを開始..."
	@bash scripts/setup.sh

install: ## 依存関係のみインストール（仮想環境は既に存在する前提）
	@echo "→ 依存関係をインストール中..."
	@if [ ! -d ".venv" ]; then \
		echo "エラー: 仮想環境が見つかりません。先に 'make setup' を実行してください。"; \
		exit 1; \
	fi
	@if command -v uv >/dev/null 2>&1; then \
		uv pip install -e .; \
	else \
		$(VENV_PIP) install -e .; \
	fi
	@echo "✓ 依存関係のインストール完了"

check: ## 依存関係の確認
	@echo "→ 依存関係を確認中..."
	@if [ ! -d ".venv" ]; then \
		echo "エラー: 仮想環境が見つかりません。先に 'make setup' を実行してください。"; \
		exit 1; \
	fi
	@$(VENV_PYTHON) scripts/check_dependencies.py

build: ## プレゼンテーションをビルド (使用例: make build SCRIPT=scripts/generate_presentation.py)
	@if [ -z "$(SCRIPT)" ]; then \
		echo "エラー: SCRIPTパラメータが必要です。"; \
		echo "使用例: make build SCRIPT=scripts/generate_presentation.py"; \
		exit 1; \
	fi
	@if [ ! -f "$(SCRIPT)" ]; then \
		echo "エラー: スクリプトが見つかりません: $(SCRIPT)"; \
		exit 1; \
	fi
	@echo "→ プレゼンテーションをビルド中: $(SCRIPT)"
	@mkdir -p $(OUTPUT_DIR)
	@$(VENV_PYTHON) $(SCRIPT)
	@echo "✓ ビルド完了"

examples: ## サンプルプレゼンテーションを生成
	@echo "→ サンプルプレゼンテーションを生成中..."
	@mkdir -p $(OUTPUT_DIR)
	@if [ -f "examples/architecture_example.py" ]; then \
		echo "  - Architecture examples..."; \
		$(VENV_PYTHON) examples/architecture_example.py; \
	fi
	@if [ -f "examples/full_presentation_example.py" ]; then \
		echo "  - Full presentation example..."; \
		$(VENV_PYTHON) examples/full_presentation_example.py; \
	fi
	@echo "✓ サンプル生成完了"

test: ## テストを実行（将来の実装用）
	@echo "→ テストを実行中..."
	@if [ -d "tests" ] && [ -n "$$(ls -A tests/*.py 2>/dev/null)" ]; then \
		$(VENV_PYTHON) -m pytest tests/; \
	else \
		echo "テストファイルが見つかりません。"; \
	fi

clean: ## 生成ファイルをクリーンアップ
	@echo "→ クリーンアップ中..."
	@rm -rf $(OUTPUT_DIR)/*.pptx
	@rm -rf $(OUTPUT_DIR)/diagrams/*.png
	@rm -rf versions/*.pptx
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✓ クリーンアップ完了"

clean-all: clean ## すべての生成物と仮想環境を削除
	@echo "→ 仮想環境も含めて削除中..."
	@rm -rf .venv venv
	@rm -rf *.egg-info
	@rm -rf build dist
	@echo "✓ すべてクリーンアップ完了"

list-scripts: ## scripts/ディレクトリのプレゼンテーション生成スクリプト一覧
	@echo "利用可能なプレゼンテーション生成スクリプト:"
	@echo ""
	@find scripts -name "generate_*.py" -o -name "create_*.py" 2>/dev/null | while read script; do \
		echo "  $$script"; \
	done || echo "  (まだスクリプトがありません)"
	@echo ""
	@echo "使用例: make build SCRIPT=scripts/generate_presentation.py"

watch: ## ファイル変更を監視して自動ビルド（要: entr）
	@if ! command -v entr >/dev/null 2>&1; then \
		echo "エラー: 'entr' コマンドが必要です。"; \
		echo "インストール: sudo apt-get install entr (Ubuntu)"; \
		echo "           brew install entr (macOS)"; \
		exit 1; \
	fi
	@if [ -z "$(SCRIPT)" ]; then \
		echo "エラー: SCRIPTパラメータが必要です。"; \
		echo "使用例: make watch SCRIPT=scripts/generate_presentation.py"; \
		exit 1; \
	fi
	@echo "→ ファイル変更を監視中（Ctrl+Cで終了）..."
	@echo "  監視対象: $(SCRIPT)"
	@echo $(SCRIPT) | entr make build SCRIPT=$(SCRIPT)

.PHONY: dev
dev: setup check ## 開発環境のセットアップ（setup + check）
	@echo "✓ 開発環境の準備完了"
