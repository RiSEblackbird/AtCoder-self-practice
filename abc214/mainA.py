# A - New Generation ABC
# https://atcoder.jp/contests/abc214/tasks/abc214_a
# 提出AC
# https://atcoder.jp/contests/abc214/submissions/27573568
N = int(input())
bottom = [1,126,212]
upper = [125,211,214]
check = [4, 6, 8]
for i in range(3):
  if bottom[i] <= N <= upper[i]:
    ans = check[i]
    break

print(ans)

# 範囲マッチ
