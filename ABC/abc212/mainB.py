# B - Weak Password https://atcoder.jp/contests/abc212/tasks/abc212_b
# 提出AC https://atcoder.jp/contests/abc212/submissions/27705840
X = input()
nums = "0123456789012"

if (len(set(list(X))) == 1) or (X in nums):
  print("Weak")
else:
  print("Strong")

# WA
# memo
# 「1 <= i <= 3」, 「X[i+1]がX[i]の次の数字である」 の意味を間違えてとらえてた。
# 登場する数字は[i, i+1] = [1,2],[2,3],[3,4] なので４文字並んで数え番号になっていることが条件。
# ４文字のうち３文字だと勘違いして下記の解答をしていた。
X = list(input())
nums = "0123456789012"

if len(set(X)) != 1:
  for i in range(2):
    ans = "Weak" if "".join(X[i:i+3]) in nums else "Strong"
else:
  ans = "Weak"

print(ans)

# memo 上記解答では不使用
# 一桁の整数について1ずつ増加させて繰り上がりを判定する際、9 + 1 = 10 であることを念頭に置く
# 桁が上がるなら n % 10 == 0, 上がらないなら n % 10 == n となる。

# memo 今回
# 3連続の数値のパターンが1パターンの文字列 "0123456789012" に含まれるのでそれを使う。

# 数値パターン 繰り上がり
