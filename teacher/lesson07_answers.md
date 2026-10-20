# 第7回 解答・指導メモ

## 00_review.py

- `items[0]` → `Potion`
- `len(items)` → `3`
- for文 → `持ち物: Potion` / `持ち物: Sword` / `持ち物: Bow`（3つ目が`Bow`に変わっていることがポイント）

## 01_append.py

| 問題 | 答え |
|---|---|
| 問題1 予想 | `['Potion', 'Sword']` |
| 問題1 自力 | `bag.append("Shield")` → `print(bag)` |
| 問題2 | 自力課題をやっていれば`3`、やっていなければ`2`。`append()`1回で`len()`は1増える |
| 問題3 予想 | `[1, 2, 3, 4, 5]` |
| 問題3 自力 | `tens = []` → `for i in range(1, 6): tens.append(i * 10)` |
| 問題4 自力 | `count = int(input("何人？: "))` → `for i in range(count):` |

**つまずき**：`bag = bag.append("Potion")`と書いて`None`になる生徒がいる。「appendはリストそのものを変える命令なので、`=`はいらない」と説明する。

## 02_in_remove.py

| 問題 | 答え |
|---|---|
| 問題1 予想 | `True` / `False`、続けて`扉を開けた！` |
| 問題1 自力 | `if "Map" in bag:` … `else:` → `地図がない…` |
| 問題2 自力 | `if "Sword" not in bag:` → Swordを持っているので何も表示されない |
| 問題3 予想 | `['Sword', 'Potion', 'Key']`（最初のPotionだけ消える） |
| 問題4 | `ValueError: list.remove(x): x not in list`。`if "Map" in bag: bag.remove("Map")` `else: print("Mapは持っていない")` |
| 問題5 | `apend` → `append`。`AttributeError: 'list' object has no attribute 'apend'` |

**板書**：`in`は「調べるだけ（変えない）」、`append`・`remove`は「リストを変える」。

## 03_challenge.py

模範解答：[lesson07/03_challenge_answer.py](lesson07/03_challenge_answer.py)
発展1〜3：[lesson07/03_challenge_advanced_answer.py](lesson07/03_challenge_advanced_answer.py)

**つまずき**

- while文の中で`input()`し直さず無限ループ → `Ctrl + C`で止め方を全体に共有してから始める
- `while item != "end":`の`!=`を忘れている生徒が多い → 第2回の比較演算子を思い出させる
- `print(item, "を買った！")`を`if`の外に書き、ない商品でも「買った」と出る → インデントを確認

**発展の答え方の例**：`if`・`elif`・`elif`・`else`の順番が大切（「商品がない」→「もう持っている」→「お金が足りない」→ 買える）。

## 04_trace.py

| 処理 | bag | len(bag) |
|---|---|---|
| 最初 | `['Potion']` | 1 |
| `append("Key")`の後 | `['Potion', 'Key']` | 2 |
| `append("Potion")`の後 | `['Potion', 'Key', 'Potion']` | 3 |
| `remove("Potion")`の後 | `['Key', 'Potion']` | 2 |
| if文の後 | `['Key', 'Potion', 'Ether']` | 3 |

`"Potion" in bag`は`True`（2つ目のPotionが残っている）。表示は`['Key', 'Potion', 'Ether']`と`3`。

**ねらい**：`remove()`が最初の1つだけ消すことを、もう一度確認させる。
