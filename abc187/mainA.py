# A - Large Digits
# https://atcoder.jp/contests/abc187/tasks/abc187_a
# 提出AC
# https://atcoder.jp/contests/abc187/submissions/27606457
A,B = map(str, list(input().split()))
a = list(map(int, A))
b = list(map(int, B))
print( sum(a) if sum(a) >= sum(b) else sum(b) )

# 総和 sum()
