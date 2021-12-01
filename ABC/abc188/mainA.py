# A - Three-Point Shot
# https://atcoder.jp/contests/abc188/tasks/abc188_a
# 提出AC
# https://atcoder.jp/contests/abc188/submissions/27606029
x,y = map(int, input().split())
diff = abs(x-y)
print( "Yes" if diff < 3 else "No" )

# 絶対値
