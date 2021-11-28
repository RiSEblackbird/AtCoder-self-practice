# A - Exact Price
# https://atcoder.jp/contests/abc223/tasks/abc223_a
# 提出AC
# https://atcoder.jp/contests/abc223/submissions/27564484
X = list(input())

ans = "No"
if len(X) >= 3 and X[-1] == "0" and X[-2] == "0":
  ans = "Yes"

print(ans)
