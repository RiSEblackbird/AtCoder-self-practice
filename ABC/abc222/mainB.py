# B - Failing Grade
# https://atcoder.jp/contests/abc222/tasks/abc222_b
# 提出AC
# https://atcoder.jp/contests/abc222/submissions/27632343
n,p = map(int, input().split())
l = list(map(int, input().split()))

c = 0
for a in l:
  c += 1 if a < p else 0

print(c)
