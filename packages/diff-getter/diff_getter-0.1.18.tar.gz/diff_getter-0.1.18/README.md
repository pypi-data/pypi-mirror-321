# diff-getter

テキスト文字列間の差分を取得するシンプルなPythonユーティリティです。異なる形式（unified形式とcontext形式）での差分出力をサポートしています。

## 特徴

- 2つのテキスト文字列間の差分を簡単に取得
- unified形式とcontext形式の両方をサポート
- リスト形式または文字列形式での差分出力
- Pythonライブラリとしての使用、またはコマンドラインツールとしての使用が可能

## インストール

pipを使用してインストールできます：

```bash
pip install diff-getter
```

## 使用方法

### Pythonライブラリとして

#### Unified形式の差分を取得

```python
from diff_getter import get_unified_diff, get_unified_diff_string

# テキストの準備
text1 = "これはテストです。\n1行目\n2行目\n3行目"
text2 = "これはテストです。\n1行目\n2行目（変更）\n4行目"

# リスト形式で差分を取得
diff_list = get_unified_diff(text1, text2)
print(diff_list)
# 出力:
# ['--- 変更前', '+++ 変更後', '@@ -1,4 +1,4 @@',
#  ' これはテストです。', ' 1行目', '-2行目', '-3行目',
#  '+2行目（変更）', '+4行目']

# 文字列形式で差分を取得
diff_string = get_unified_diff_string(text1, text2)
print(diff_string)
# 出力:
# --- 変更前
# 
# +++ 変更後
# 
# @@ -1,4 +1,4 @@
# 
#  これはテストです。
#  1行目
# -2行目
# -3行目
# +2行目（変更）
# +4行目
```

#### Context形式の差分を取得

```python
from diff_getter import get_context_diff, get_context_diff_string

# テキストの準備
text1 = "これはテストです。\n1行目\n2行目\n3行目"
text2 = "これはテストです。\n1行目\n2行目（変更）\n4行目"

# リスト形式で差分を取得
diff_list = get_context_diff(text1, text2)
print(diff_list)
# 出力:
# ['*** 変更前', '--- 変更後', '***************',
#  '*** 1,4 ****', '  これはテストです。', '  1行目',
#  '! 2行目', '! 3行目', '--- 1,4 ----',
#  '  これはテストです。', '  1行目', '! 2行目（変更）',
#  '! 4行目']

# 文字列形式で差分を取得
diff_string = get_context_diff_string(text1, text2)
print(diff_string)
# 出力:
# *** 変更前
# --- 変更後
# ***************
# *** 1,4 ****
#   これはテストです。
#   1行目
# ! 2行目
# ! 3行目
# --- 1,4 ----
#   これはテストです。
#   1行目
# ! 2行目（変更）
# ! 4行目
```

### コマンドラインツール

```bash
# Unified形式で差分を取得
diff-getter unified 古いテキストのファイルパス 新しいテキストのファイルパス

# Context形式で差分を取得
diff-getter context 古いテキストのファイルパス 新しいテキストのファイルパス
```

## 開発者向け情報

### 必要条件

- Python 3.10以上
- uv（依存関係管理ツール）

### 開発環境のセットアップ

1. リポジトリのクローン：
```bash
git clone https://github.com/tatn/diff-getter-python.git
cd diff-getter
```

2. 仮想環境の作成と有効化：
```bash
uv venv --python 3.10
.venv\Scripts\activate  # Windows
```

3. 開発用依存パッケージのインストール：
```bash
uv add --dev pytest pytest-cov black ruff mypy build twine hatch
```

### 品質管理

#### テストの実行

```bash
# 通常のテスト実行
uv run pytest

# カバレッジレポート付きでテストを実行
uv run pytest --cov=diff_getter tests/
```

#### コード品質チェック

```bash
# コードフォーマット
uv run black .

# リンター
uv run ruff check .

# 型チェック
uv run mypy src/diff_getter
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
