# A - Registration
# https://atcoder.jp/contests/abc167/tasks/abc167_a
# 提出AC
# https://atcoder.jp/contests/abc167/submissions/27619222
s = list(str(input()))
t = list(str(input()))
if len(s) == len(t) - 1 and s == t[0:-1]:
  print("Yes")
else:
  print("No")
