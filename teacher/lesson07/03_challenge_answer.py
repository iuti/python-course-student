# 第7回 自力課題 模範解答（講師用）

shop_items = ["Potion", "Ether", "Sword", "Shield"]
bag = []

print("いらっしゃい！")
print("売っているもの:", shop_items)

item = input("買うもの(終わるときは end): ")

while item != "end":
    if item in shop_items:
        bag.append(item)
        print(item, "を買った！")
    else:
        print("そんな商品はないよ")
    item = input("買うもの(終わるときは end): ")

print("バッグの中身:", bag)
print("アイテム数:", len(bag))
