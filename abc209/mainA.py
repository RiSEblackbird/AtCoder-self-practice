# A - Counting
# https://atcoder.jp/contests/abc209/tasks/abc209_a
# 提出AC
# https://atcoder.jp/contests/abc209/submissions/27580043
a,b = map(int, input().split())
if a < b:
  print(b-a+1)
else:
  print(0)
