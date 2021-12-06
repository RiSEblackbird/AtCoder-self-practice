# B - Nuts https://atcoder.jp/contests/abc204/tasks/abc204_b
# 提出AC https://atcoder.jp/contests/abc204/submissions/27743379
N = int(input())
A = list(map(int, input().split()))

score = 0
for a in range(N):
  if a > 10:
    score += (a - 10)

print(score)
