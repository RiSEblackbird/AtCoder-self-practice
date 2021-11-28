# A - Lexicographic Order
# https://atcoder.jp/contests/abc217/tasks/abc217_a
# 提出AC
# https://atcoder.jp/contests/abc217/submissions/27567906
S,T = input().split(" ")
list = sorted([S,T])
ans = "Yes" if list == [S,T] else "No"
print(ans)
