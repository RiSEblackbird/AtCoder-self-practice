# A - Tiny Arithmetic Sequence
# https://atcoder.jp/contests/abc201/tasks/abc201_a
# 提出AC
# https://atcoder.jp/contests/abc201/submissions/27592175
a,b,c = map(int, input().split())
list = sorted([a,b,c])
if (list[2] - list[1]) == (list[1] - list[0]):
  print("Yes")
else:
  print("No")

# 等差数列
