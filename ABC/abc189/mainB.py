# B - Alcoholic https://atcoder.jp/contests/abc189/tasks/abc189_b
# 提出AC https://atcoder.jp/contests/abc189/submissions/27961013
N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]
X100 = X*100
ans100 = 0
for i in range(N):
  ans100 += VP[i][0]*VP[i][1]
  if ans100 > X100:
    print(i+1)
    break
  elif i == N-1:
    print(-1)

# リファクタ 提出AC https://atcoder.jp/contests/abc189/submissions/27961325
N, X = map(int, input().split())
X100 = X * 100
ans100 = 0
for i in range(N):
  V, P = map(int, input().split())
  ans100 += V * P
  if ans100 > X100: print(i+1); exit()
print(-1)
