# C - Counting 2 https://atcoder.jp/contests/abc231/tasks/abc231_c
# 提出AC https://atcoder.jp/contests/abc231/submissions/27915848
import bisect
N,Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(int(input()) for _ in range(Q))

A.sort()
for j in range(Q):
  print( N-bisect.bisect_left(A,X[j]) )

# コンテ中 TLE ループごり押しだと計算時間がオーバーする
N,Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(int(input()) for _ in range(Q))

for j in range(Q):
  print( sum(map(lambda a: a-X[j] >= 0, A)) )

# 二分探索 bisect
