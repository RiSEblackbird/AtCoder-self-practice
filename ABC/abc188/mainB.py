# B - Orthogonality https://atcoder.jp/contests/abc188/tasks/abc188_b
# 提出AC https://atcoder.jp/contests/abc188/submissions/27961497
# Easy
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = [ A[_]*B[_] for _ in range(N) ]
print("NYoe s"[(sum(AB) == 0)::2])

# リファクタ 提出AC https://atcoder.jp/contests/abc188/submissions/27961645
input()
ABsum = sum(map(lambda a,b: a*b, map(int, input().split()), map(int, input().split())))
print("NYoe s"[(ABsum == 0)::2])
