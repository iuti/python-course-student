# 第9回 発展課題1・2 模範解答（講師用）

names = ["Slime", "Bat", "Golem", "Dragon"]
hps = [30, 45, 120, 300]
defenses = [0, 5, 20, 50]

# 注意：ダメージがDragonの防御力50以下だと永遠に終わらない（Ctrl + C で止める）。
# 生徒が無限ループになったら「なぜ終わらない？」を考えさせるチャンス。
damage = int(input("全体攻撃のダメージ: "))
turn = 0

while sum(hps) > 0:
    turn = turn + 1
    print("---", turn, "ターン目 ---")
    for i in range(len(hps)):
        if hps[i] > 0:
            real_damage = damage - defenses[i]
            if real_damage < 0:
                real_damage = 0
            hps[i] = hps[i] - real_damage
            if hps[i] <= 0:
                hps[i] = 0
                print(names[i], "をたおした！")
            else:
                print(names[i], "の残りHP:", hps[i])

print(turn, "ターンで全滅させた！")
