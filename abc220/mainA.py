# A - Find Multiple
# https://atcoder.jp/contests/abc220/tasks/abc220_a
# 提出AC
# https://atcoder.jp/contests/abc220/submissions/27567038


A,B,C = map(int, input().split(" "))

ans = -1
for i in range(int(1000/C)+1):
  if A <= C*i and C*i <= B:
    ans = C*i
    break

print(ans)

# 以上、以下　範囲
