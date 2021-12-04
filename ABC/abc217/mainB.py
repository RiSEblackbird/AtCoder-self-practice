# B - AtCoder Quiz
# https://atcoder.jp/contests/abc217/tasks/abc217_b
# 提出AC
# https://atcoder.jp/contests/abc217/submissions/27685330
S = set(input() for _ in range(3))
ans = {"ABC", "ARC", "AGC","AHC"} - S
print(*ans)

# 要素マッチ
