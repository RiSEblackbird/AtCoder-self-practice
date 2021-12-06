# B - Permutation Check https://atcoder.jp/contests/abc205/tasks/abc205_b
# 提出AC https://atcoder.jp/contests/abc205/submissions/27743263
N = int(input())
A = list(input().split())

ans = "Yes" if N == len(set(A)) else "No"
print(ans)
