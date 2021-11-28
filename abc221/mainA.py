# A - Seismic magnitude scales
# https://atcoder.jp/contests/abc221/tasks/abc221_a
# 提出AC
# https://atcoder.jp/contests/abc221/submissions/27566022
A,B = map(int, input().split(" "))
level_diff = A-B
ans = 32 ** level_diff
print(ans)
