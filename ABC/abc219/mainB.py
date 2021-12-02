# B - Maritozzo
# https://atcoder.jp/contests/abc219/tasks/abc219_b
# 提出AC
# https://atcoder.jp/contests/abc219/submissions/27634033
S = [input() for _ in range(3)]
T = list(input())

l = [];
for t in T:
  l.append(S[int(t)-1])
print("".join(l))
