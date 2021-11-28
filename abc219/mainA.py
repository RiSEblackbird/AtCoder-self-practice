# A - AtCoder Quiz 2
# https://atcoder.jp/contests/abc219/tasks/abc219_a
# 提出AC
# https://atcoder.jp/contests/abc219/submissions/27567354

X = int(input())

upper = [40, 70, 90]
bottom = [0, 40, 70]

for i in range(3):
  if 90 <= X:
    ans = "expert"
    break
  if bottom[i] <= X and X < upper[i]:
    ans = upper[i] - X

print(ans)

# 範囲　合格点　得点
