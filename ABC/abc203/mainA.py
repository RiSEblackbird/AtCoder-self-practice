# A - Chinchirorin
# https://atcoder.jp/contests/abc203/tasks/abc203_a
# 提出AC
# https://atcoder.jp/contests/abc203/submissions/27591567

a,b,c = map(int, input().split())
if a == b:
  print(c)
elif b == c:
  print(a)
elif a == c:
  print(b)
else:
  print(0)

# 解説見た。ちょっと時間をおいて再回答する。
# あまり意識してなかったけど、elifで繋げてるからひとつの判定ブロックにできてるのであって、
# すべて if で繋げると3回の条件分岐になってしまう。

# さいころ
