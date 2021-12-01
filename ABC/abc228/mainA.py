# A - On and Off
# https://atcoder.jp/contests/abc228/tasks/abc228_a
# 提出AC
# https://atcoder.jp/contests/abc228/submissions/27563521
s,t,x = map(int, input().split())
if s < t:
  ans = "Yes" if s <= x < t else "No"
else:
  ans = "No" if t <= x < s else "Yes"

print(ans)

# たぶんOK　https://atcoder.jp/contests/abc228/tasks/abc228_a