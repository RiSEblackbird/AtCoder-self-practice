# A - Rock-paper-scissors
# https://atcoder.jp/contests/abc204/tasks/abc204_a
# 提出AC
# https://atcoder.jp/contests/abc204/submissions/27581361
x,y = map(int, input().split())

if x == y:
  z = x
else:
  z = 3 - x - y

print(z)

# 解説見るまで、数の引き算で対応できることに気づかなかった。
# じゃんけん
