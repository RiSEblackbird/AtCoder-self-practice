# A - Distinct Strings
# https://atcoder.jp/contests/abc225/tasks/abc225_a
# 提出AC
# https://atcoder.jp/contests/abc225/submissions/27561830

s = list(set(input()))
len = len(s)

if len == 3:
  ans = 6
elif len == 2:
  ans = 3
elif len == 1:
  ans = 1

print(ans)
