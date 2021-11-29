# A - Century
# https://atcoder.jp/contests/abc200/tasks/abc200_a
# 
# 
n = int(input())
for centry in range(31):
  if 1 + 100*(centry - 1) <= n <= 100*centry:
   print(centry)
   break

# はじめrange(29)でWAになってしまった！
# 
#   print("i={}".format(centry))

# range() 関数
# https://docs.python.org/ja/3/tutorial/controlflow.html#the-range-function
# 0～(引数-1) まで {引数}回ループするという意味。

# 暦 世紀 西暦
