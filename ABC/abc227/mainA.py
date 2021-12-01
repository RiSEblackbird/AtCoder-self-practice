# A - Last Card
# https://atcoder.jp/contests/abc227/tasks/abc227_a
# 提出AC
# https://atcoder.jp/contests/abc227/submissions/27563613
n,k,a = map(int, input().split())

if k > (n - a):
  # zk 一巡直後の残りのカード枚数
  zk = k - (n - (a -1))
  # print("zk:{}".format(zk))
  sur = zk % n
  ans = n if sur == 0 else sur
  # print("ans:{}".format(ans))
else:
  ans = a + k - 1

print(ans)

# メモの例
# [N K A] [10 8 5]
# 配り終わった図
# [1 2 3 4 5 6 7 8 9 10]
# [- -     - - - - - - ]
# ５番目からスタート
# 一巡して残りのカードは　K:8枚 - [一巡目で配る分(n-a-1):6枚] = 2枚
# 2枚から10人を分母にする剰余は２、つまりその週で２人に配って終了なので, ans = 2
# もし剰余が０の場合は、リストの最後の人でちょうど配り終わったことになるので、ans = n になる。
