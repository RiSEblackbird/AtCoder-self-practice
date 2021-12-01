# A - Maxi-Buying
# https://atcoder.jp/contests/abc206/tasks/abc206_a
# 提出AC
# https://atcoder.jp/contests/abc206/submissions/27580597
N = int(input())
price_list = str(N*1.08).split(".")
price = int(price_list[0])
target = 206
if price < target:
  print("Yay!")
elif price == target:
  print("so-so")
else:
  print(":(")

## 備考：小数計算を避けるために 1.08 を100倍して計算を進めたほうが良かった
# 小数
