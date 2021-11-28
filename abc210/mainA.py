# A - Cabbages
# https://atcoder.jp/contests/abc210/tasks/abc210_a
# 提出AC
# https://atcoder.jp/contests/abc210/submissions/27579598
N,A,X,Y = map(int, input().split())

if A < N:
  ans = X*A + Y*(N-A)
else:
  ans = X*N

print(ans)
