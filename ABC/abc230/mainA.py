# A - AtCoder Quiz 3
# https://atcoder.jp/contests/abc230/tasks/abc230_a
# 提出AC
# https://atcoder.jp/contests/abc230/submissions/27647849
n = int(input())

if n < 10:
  print("AGC00" + str(n))
elif n < 42:
  print("AGC0" + str(n))
else:
  print("AGC0" + str(n+1))

