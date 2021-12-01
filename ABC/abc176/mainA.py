# A - Takoyaki
# https://atcoder.jp/contests/abc176/tasks/abc176_a
# 提出AC
# https://atcoder.jp/contests/abc176/submissions/27608328
import math
n,x,t = map(int, input().split())
if n % x == 0:
  ans = math.floor(n/x) * t
else:
  ans = (math.floor(n/x) + 1) * t

print(ans)

# 切り捨て
