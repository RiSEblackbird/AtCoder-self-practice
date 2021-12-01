# A - We Love Golf
# https://atcoder.jp/contests/abc165/tasks/abc165_a
# 提出AC
# https://atcoder.jp/contests/abc165/submissions/27620505

# 1時間以上ずっと "OK","NG" を  "Yes" "No"　だと間違えて6連続WAした
# 食後で胃が張って意識朦朧の時が注意力ゼロで辛すぎる
import math
k = int(input())
a,b = map(int, input().split())

ans = "NG"
start = math.floor(a/k)
for i in range(b):
  if a <= (start + i)*k <= b:
    ans = "OK"

print(ans)

# WA
k = int(input())
a,b = map(int, input().split())
if (b-k/k)*k >= a:
  print("Yes")
else:
  print("No")

# WA 
k = int(input())
a,b = map(int, input().split())
n = b - k
if a % k == 0 or b % k == 0:
  print("OK")
elif (b-k)/k >= a:
  print("OK")
else:
  print("NG")

# 倍数
