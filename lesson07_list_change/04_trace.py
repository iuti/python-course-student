# 第7回 トレース問題
# 最初は実行せず、下の表を紙やノートに書いて完成させましょう。

bag = ["Potion"]

bag.append("Key")
bag.append("Potion")
bag.remove("Potion")

if "Potion" in bag:
    bag.append("Ether")

print(bag)
print(len(bag))


# 変数の変化
#
# | 処理                        | bag                  | len(bag) |
# |-----------------------------|----------------------|----------|
# | 最初                        | ['Potion']           | 1        |
# | bag.append("Key")の後       |                      |          |
# | bag.append("Potion")の後    |                      |          |
# | bag.remove("Potion")の後    |                      |          |
# | if文の後                    |                      |          |
#
# "Potion" in bag は True？ False？：
# 最後に表示されるリスト：
# 最後に表示される数：
