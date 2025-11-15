#!/usr/bin/env python3
"""
依存関係チェックスクリプト

このプロジェクトに必要な依存関係がすべてインストールされているか確認します。
"""

import sys
import shutil
from typing import Tuple, List

def check_python_package(package_name: str, import_name: str = None) -> Tuple[bool, str]:
    """
    Pythonパッケージがインストールされているか確認

    Args:
        package_name: パッケージ名（表示用）
        import_name: インポート名（package_nameと異なる場合）

    Returns:
        (成功フラグ, メッセージ)
    """
    if import_name is None:
        import_name = package_name.replace('-', '_')

    try:
        __import__(import_name)
        return True, f"✓ {package_name}"
    except ImportError:
        return False, f"✗ {package_name} - Not installed"

def check_system_command(command: str, package_name: str) -> Tuple[bool, str]:
    """
    システムコマンドが利用可能か確認

    Args:
        command: コマンド名
        package_name: パッケージ名（表示用）

    Returns:
        (成功フラグ, メッセージ)
    """
    if shutil.which(command):
        return True, f"✓ {package_name} (system)"
    else:
        return False, f"✗ {package_name} (system) - Not installed"

def main():
    """依存関係チェックのメイン処理"""
    print("=" * 60)
    print("PresentationTemplate - 依存関係チェック")
    print("=" * 60)
    print()

    # チェック項目
    checks: List[Tuple[bool, str]] = []

    print("【Pythonパッケージ】")
    packages = [
        ("python-pptx", "pptx"),
        ("diagrams", "diagrams"),
        ("graphviz", "graphviz"),
        ("networkx", "networkx"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("plotly", "plotly"),
        ("Pillow", "PIL"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("PyYAML", "yaml"),
        ("click", "click"),
        ("rich", "rich"),
        ("python-dateutil", "dateutil"),
    ]

    for pkg_name, import_name in packages:
        success, msg = check_python_package(pkg_name, import_name)
        checks.append((success, msg))
        print(f"  {msg}")

    print()
    print("【システムソフトウェア】")

    # Graphviz (重要)
    success, msg = check_system_command("dot", "Graphviz")
    checks.append((success, msg))
    print(f"  {msg}")

    print()
    print("=" * 60)

    # 結果サマリー
    failed = [msg for success, msg in checks if not success]

    if not failed:
        print("✓ すべての依存関係がインストールされています！")
        print()
        return 0
    else:
        print(f"✗ {len(failed)}個の依存関係が不足しています:")
        print()
        for msg in failed:
            print(f"  {msg}")
        print()
        print("【解決方法】")
        print()

        # Pythonパッケージの不足
        python_missing = [msg for msg in failed if "system" not in msg]
        if python_missing:
            print("Pythonパッケージをインストール:")
            print("  uv pip install -r requirements.txt")
            print("  または: pip install -r requirements.txt")
            print()

        # システムソフトウェアの不足
        if any("Graphviz" in msg for msg in failed):
            print("Graphvizシステムソフトウェアをインストール:")
            print("  Ubuntu/Debian: sudo apt-get install graphviz")
            print("  macOS: brew install graphviz")
            print("  Windows: https://graphviz.org/download/")
            print()

        print("詳細: TROUBLESHOOTING.md を参照")
        print()
        return 1

if __name__ == "__main__":
    sys.exit(main())
