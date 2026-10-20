# 第8回 復習：前回のリスト
# 最初は実行せず、表示される内容を予想しましょう。

scores = [70, 40, 90]
scores.append(60)

total = 0

for score in scores:
    total = total + score

print(scores)
print(len(scores))
print(total)

if 100 in scores:
    print("満点の人がいる！")
else:
    print("満点の人はいない")


# 予想
# 1行目に表示されるリスト：
# 2行目に表示される数：
# 3行目に表示される数：
# 4行目に表示される文：
