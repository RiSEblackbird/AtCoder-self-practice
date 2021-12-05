# B - Booby Prize https://atcoder.jp/contests/abc213/tasks/abc213_b
# 提出AC https://atcoder.jp/contests/abc213/submissions/27702143
N = int(input())
A = list(map(int, input().split()))

ans = A.index(sorted(A)[-2]) + 1
print(ans)

# インデックス index(), ソート(リスト新規生成) sorted()
