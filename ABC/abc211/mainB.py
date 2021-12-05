# B - Cycle Hit https://atcoder.jp/contests/abc211/tasks/abc211_b
# 提出AC https://atcoder.jp/contests/abc211/submissions/27709032
S = [input() for _ in range(4)]
pencils = {"H", "2B", "3B", "HR"}
print( "Yes" if set(S) == pencils else "No" )
