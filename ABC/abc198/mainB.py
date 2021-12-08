# B - Palindrome with leading zeros https://atcoder.jp/contests/abc198/tasks/abc198_b
# 提出AC https://atcoder.jp/contests/abc198/submissions/27771676
N = input().rstrip("0")
print( "Yes" if N == N[::-1] else "No" )

# 文字列 対称性 反転
