# A - Vanishing Pitch
# https://atcoder.jp/contests/abc191/tasks/abc191_a
# 提出AC
# https://atcoder.jp/contests/abc191/submissions/27595267
v,t,s,d = map(int, input().split())
if d < v * t or v * s < d:
  print("Yes")
else:
  print("No")

# 速度
