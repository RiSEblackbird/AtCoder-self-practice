# B - A Reverse https://atcoder.jp/contests/abc233/tasks/abc233_b
# AC https://atcoder.jp/contests/abc233/submissions/28126731
L, R = map(int, input().split())
S = list(input())
re = list(reversed(S[(L-1):R]))
S[(L-1):R] = re
print("".join(S))
