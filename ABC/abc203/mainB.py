# B - AtCoder Condominium https://atcoder.jp/contests/abc203/tasks/abc203_b
# 提出AC https://atcoder.jp/contests/abc203/submissions/27743599
N,K = map(int, input().split())

ans = 0
for n in range(N):
  for k in range(K):
    ans += ( (n+1)*100 + (k+1) )

print(ans)
