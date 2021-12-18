# B - Magic 3 https://atcoder.jp/contests/abc190/tasks/abc190_b
# 提出AC https://atcoder.jp/contests/abc190/submissions/27959067
N, S, D = map(int, input().split())

ans = "No"
for i in range(N):
  X, Y = list(map(int, input().split()))
  if X < S and Y > D:
    ans = "Yes"

print(ans)

### 別解 提出AC https://atcoder.jp/contests/abc190/submissions/27960164
N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
print( "NYoe s"[any(XY[i][0] < S and XY[i][1] > D for i in range(N))::2] )
