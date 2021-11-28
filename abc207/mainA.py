# A - Repression
# https://atcoder.jp/contests/abc207/tasks/abc207_a
# 提出AC
# https://atcoder.jp/contests/abc207/submissions/27580487
A,B,C = map(int, input().split())
ordered = sorted([A,B,C], reverse=True)
print(ordered[0]+ordered[1])

# 降順 ソート
