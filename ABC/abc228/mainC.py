# C - Final Day https://atcoder.jp/contests/abc228/tasks/abc228_c
# 提出AC https://atcoder.jp/contests/abc228/submissions/me
N,K = map(int, input().split())
P = [sum(list(map(int, input().split()))) for n in range(N) ]
p = sorted(P, reverse=True)[K-1]
print( *["\nYes" if P[i]+300 >= p else "\nNo" for i in range(N)] )
# 閾値の点数を求めて、4日目の点数と比較する


# WA
import bisect
N,K = map(int, input().split())
P = [sum(list(map(int, input().split()))) for n in range(N) ]
S = sorted(P)
print( *["\nYes" if (N - bisect.bisect_left(S,P[i]+300)) <= K else "\nNo" for i in range(N)] )

# 順位 序列

