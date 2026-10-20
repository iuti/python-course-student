# 第8回 発展課題2・3 模範解答（講師用）

scores = [1200, 850, 2300, 400, 1750, 980, 3100, 1420]

my_score = int(input("あなたの得点: "))
scores.append(my_score)

print("参加人数:", len(scores))
print("平均点:", sum(scores) / len(scores))

higher = 0
for score in scores:
    if score > my_score:
        higher = higher + 1

print("あなたは", higher + 1, "位です")
