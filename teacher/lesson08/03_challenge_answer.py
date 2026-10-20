# 第8回 自力課題 模範解答（講師用）

scores = [1200, 850, 2300, 400, 1750, 980, 3100, 1420]

print("参加人数:", len(scores))

total = 0
for score in scores:
    total = total + score
print("合計点:", total)

average = total / len(scores)
print("平均点:", average)

print("最高点:", max(scores))
print("最低点:", min(scores))

count = 0
for score in scores:
    if score >= 1000:
        count = count + 1
print("1000点以上の人数:", count)

high_scores = []
for score in scores:
    if score >= 1000:
        high_scores.append(score)
print("high_scores:", high_scores)

# 発展課題1
above_average = 0
for score in scores:
    if score >= average:
        above_average = above_average + 1
print("平均点以上の人数:", above_average)
