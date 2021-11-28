# A - Four Digits
# https://atcoder.jp/contests/abc222/tasks/abc222_a
# 提出AC
# https://atcoder.jp/contests/abc222/submissions/27565598

N = list(input())

if len(N) < 4:
  for i in range(4-len(N)):
    N.insert(0, "0")
  
ans = "".join(N)
print(ans)