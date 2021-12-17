# B - uNrEaDaBlE sTrInG https://atcoder.jp/contests/abc192/tasks/abc192_b
# 提出AC https://atcoder.jp/contests/abc192/submissions/27955672
S = input()

lo = S[::2]
up = S[1::2]
print( "Yes" if lo.lower() == lo and up.upper() == up else "No" )

# 大文字 小文字
