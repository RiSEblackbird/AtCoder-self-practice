# B - Savings https://atcoder.jp/contests/abc206/tasks/abc206_b
# 提出AC https://atcoder.jp/contests/abc206/submissions/27742686
N = int(input())
s = 0
ans = 0
for i in range(1000000):
  s += i+1
  if s >= N:
    ans = i+1
    break

print(ans)
