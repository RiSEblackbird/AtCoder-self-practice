# A - Payment
# https://atcoder.jp/contests/abc173/tasks/abc173_a
# 提出AC
# https://atcoder.jp/contests/abc173/submissions/27608647
n = int(input())
print( 1000 - (n % 1000) if n % 1000 != 0 else 0 )

# [WA] memo: 割り切れるときを考慮してなかった
n = int(input())
print( 1000 - (n % 1000) )

# お釣り 剰余
