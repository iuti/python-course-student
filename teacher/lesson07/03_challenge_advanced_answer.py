# 第7回 発展課題1〜3 模範解答（講師用）

shop_items = ["Potion", "Ether", "Sword", "Shield"]
bag = []
money = 100
price = 30

print("いらっしゃい！")
print("売っているもの:", shop_items, "どれも", price, "ゴールド")

item = input("買うもの(終わるときは end): ")

while item != "end":
    if item not in shop_items:
        print("そんな商品はないよ")
    elif item in bag:
        print("もう持っているよ")
    elif money < price:
        print("お金が足りない！")
    else:
        bag.append(item)
        money = money - price
        print(item, "を買った！ 残り", money, "ゴールド")
    item = input("買うもの(終わるときは end): ")

print("バッグの中身:", bag)
print("アイテム数:", len(bag))
print("残りのお金:", money)

sell = input("売るもの: ")
if sell in bag:
    bag.remove(sell)
    print(sell, "を売った！")
else:
    print(sell, "は持っていない")
print("バッグの中身:", bag)
