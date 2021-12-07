# B - 200th ABC-200 https://atcoder.jp/contests/abc200/tasks/abc200_b
# 提出AC https://atcoder.jp/contests/abc200/submissions/27757376
N,K = map(int, input().split())
for i in range(K):
  if N % 200 == 0:
    N //= 200
  else:
    N = int((str(N)) + "200")
print(N)

# ただ割るだけだと小数点が入って破綻する
# N /= 200
# N=2021
# N=2021200
# N=10106.0
