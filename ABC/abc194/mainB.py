# B - Job Assignment https://atcoder.jp/contests/abc194/tasks/abc194_b
# 提出AC https://atcoder.jp/contests/abc194/submissions/27944872
N = int(input())
A = [0]*N
B = [0]*N

for i in range(N):
  A[i], B[i] = map(int, input().split())

ans = min( [ max([A[i],B[j]]) if i != j else A[i] + B[j] for i in range(N) for j in range(N) ] )
print(ans)
