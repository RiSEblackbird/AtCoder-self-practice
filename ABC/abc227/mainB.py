# B - KEYENCE building
# https://atcoder.jp/contests/abc227/tasks/abc227_b

## Give up
## 入出力例をクリアできず、後日
n = int(input())
s = list(map(int, input().split()))

lie_count = 0
for i in range(len(s)):
  lie_flg = True
  for a in range(1000):
    for b in range(1000):
      print("{} <-> {}".format(4*a*b + 3*a + 3*b,s[i]))
      if 4*a*b + 3*a + 3*b == s[i]:
        lie_flg = False
        break
  print(lie_flg)
  if lie_flg == True:
    lie_count += 1

print(lie_count)
