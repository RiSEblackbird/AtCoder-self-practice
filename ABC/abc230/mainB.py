# B - Triple Metre
# https://atcoder.jp/contests/abc230/tasks/abc230_b
# AC ここまで20分間
# https://atcoder.jp/contests/abc230/submissions/27655182
s = list(input())
t = list("".join( "oxx" for _ in range(100000) ))

ans = "No"
for i in range(10):
  w = t[i:i+len(s)]
  if s == w:
    ans = "Yes"
    break

print(ans)
