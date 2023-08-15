# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: record_budget
### パラメータ:
- self: BudgetBook - インスタンス自体
- selected_budgetbook: str - 選択された家計簿名
### 戻り値:
なし
### 説明:
収入または支出の記録を家計簿に行います。
### 処理内容:
- ユーザに`income`または`payment`を入力させ、変数`record_type`にセットします。
- 金額を入力させ、変数`amount`へセットします。
- 共通で使用するカラム名と値の一部を定義します。
- 収入の場合:
  - 収入源とノートを入力させます。
  - クエリ例を参考にSQLクエリを作成し、変数`query`にセットします。
  - 変数`values`へクエリ例を参考に値をセットします。
- 支出の場合:
  - カテゴリーとノートを入力させます。
  - クエリ例を参考にSQLクエリを作成し、変数`query`にセットします。
  - 変数`values`へクエリ例を参考に値をセットします。
- どちらでもない場合
  - 無効な選択です。とエラーメッセージを表示する。
- [`execute_query`](../../../db/sql.py/SQLManagerクラス/execute_query.html)メソッドへ変数`query`と`values`を渡してクエリを実行します。
- 戻り値が`True`の場合、「記録が完了しました。」のメッセージを表示します。
- 戻り値が`False`の場合、「記録に失敗しました。」のメッセージを表示します。

### データベース関連の文法解説:

```python
# 「budgetbooksテーブルから全ての列の値を取り出す。ただし抽出する行はbook_name列の値が?の行に絞り込む」という意味のクエリを作成する
query = "SELECT * FROM budgetbooks WHERE book_name = ?;"
# ('堀川の家計簿',)を変数valuesにセット
values = ('堀川の家計簿',)
# ?の部分を変数values:'堀川の家計簿'に置き換えてクエリを実行
result = self.budget.sql_manager.fetch_one(query, values)
```

#### クエリ例

```python
# 収入の場合
if record_type == 'income':
  # 変数sourceとnotesの設定
  source = input('収入源を入力してください: ')
  notes = input('ノートを入力してください (任意): ')

  # クエリ作成
  query = "INSERT INTO incomes (budgetbooks_id, amount, created_at, updated_at, source, notes) VALUES ((SELECT id FROM budgetbooks WHERE book_name = ?), ?, datetime('now', '+9 hours'), datetime('now', '+9 hours'), ?, ?);"

  values = (selected_budgetbook, amount, source, notes)

# 支出の場合の詳細入力
elif record_type == 'payment':
  # 変数categoryとnotesの設定
  category = input('カテゴリーを入力してください: ')
  notes = input('ノートを入力してください (任意): ')

  # クエリ作成
  query = "INSERT INTO payments (budgetbooks_id, amount, created_at, updated_at, category, notes) VALUES ((SELECT id FROM budgetbooks WHERE book_name = ?), ?, datetime('now', '+9 hours'), datetime('now', '+9 hours'), ?, ?);"

  values = (selected_budgetbook, amount, category, notes)

```