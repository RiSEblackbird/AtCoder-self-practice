# A - I Scream
# https://atcoder.jp/contests/abc194/tasks/abc194_a
# 提出AC
# https://atcoder.jp/contests/abc194/submissions/27594891
a,b = map(int, input().split())
if 15 <= (a+b) and 8 <= b:
  print(1)
elif 10 <= (a+b) and 3 <= b:
  print(2)
elif 3 <= (a+b):
  print(3)
else:
  print(4)
