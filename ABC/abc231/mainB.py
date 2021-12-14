# B - Election https://atcoder.jp/contests/abc231/tasks/abc231_b
# 提出AC https://atcoder.jp/contests/abc231/submissions/27826610
N = int(input())
S = list(input() for _ in range(N))
names = list(set(S))
order = list([S.count(names[i]), names[i]] for i in range(len(names)))
print(max(order)[1])
