# A - Blood Pressure
# https://atcoder.jp/contests/abc211/tasks/abc211_a
# 提出AC
# https://atcoder.jp/contests/abc211/submissions/27579051
A,B = map(int, input().split())
print( round(((A-B)/3)+B, 6) )

# 丸める 小数点