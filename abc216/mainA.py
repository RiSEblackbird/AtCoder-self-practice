# A - Signed Difficulty
# https://atcoder.jp/contests/abc216/tasks/abc216_a
# 提出AC
# https://atcoder.jp/contests/abc216/submissions/27571189
X,Y = map(int, input().split("."))
bottom = [0,3,7]
upper = [2,6,9]
check = ["-", "", "+"]
for i in range(3):
  if bottom[i] <= Y <= upper[i]:
    ans = str(X) + check[i]

print(ans)
