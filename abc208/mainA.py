# A - Rolling Dice
# https://atcoder.jp/contests/abc208/tasks/abc208_a
# 提出AC
# https://atcoder.jp/contests/abc208/submissions/27580266
A,B = map(int, input().split())
if A <= B <= 6*A:
  print("Yes")
else:
  print("No")

# はじめWA
# 回数AがBより多くても実現できない

# サイコロ
