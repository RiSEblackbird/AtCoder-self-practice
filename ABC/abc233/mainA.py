# A - 10yen Stamp https://atcoder.jp/contests/abc233/tasks/abc233_a
# AC https://atcoder.jp/contests/abc233/submissions/28116104
X, Y = map(int, input().split())
if X >= Y:
  print(0)
else:
  dif = Y - X
  print( dif//10 + 1 if dif % 10 != 0 else dif//10 )
  