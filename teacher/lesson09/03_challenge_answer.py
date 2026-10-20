# 第9回 自力課題 模範解答（講師用）

names = ["Slime", "Bat", "Golem", "Dragon"]
hps = [30, 45, 120, 300]

damage = int(input("全体攻撃のダメージ: "))

defeated = 0

for i in range(len(hps)):
    hps[i] = hps[i] - damage
    if hps[i] <= 0:
        hps[i] = 0
        print(names[i], "をたおした！")
        defeated = defeated + 1
    else:
        print(names[i], "の残りHP:", hps[i])

print("たおした数:", defeated)
print("残っている敵:", len(hps) - defeated)

print(hps)
