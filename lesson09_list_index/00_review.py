# 第9回 復習：前回の集計
# 最初は実行せず、表示される内容を予想しましょう。

hps = [50, 20, 80, 30]

count = 0

for hp in hps:
    if hp >= 50:
        count = count + 1

print(count)
print(sum(hps))
print(max(hps))
print(sum(hps) / len(hps))


# 予想
# 1行目：
# 2行目：
# 3行目：
# 4行目：
#
# 考えよう：max(hps) は 80 だとわかるけれど、
#           「80 は何番目（添字いくつ）にある？」をプログラムで調べるには？
#           → 今日はこれができるようになります。
