# A - Round decimals
# https://atcoder.jp/contests/abc226/tasks/abc226_a

# 小数点　Decimal point
# x, dc = map(int, input().split("."))

print(int(round(float(input()))))
# ひとつWAになった。分解してコンマ以下の一桁目で判断するのが確実そう。

# => 提出AC
# https://atcoder.jp/contests/abc226/submissions/27563966
x = input().split(".")

if int(x[1][0]) >= 5:
  ans = int(x[0]) + 1
else:
  ans = int(x[0])

print(ans)