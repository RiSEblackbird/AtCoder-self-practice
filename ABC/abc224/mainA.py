# A - Tires
# https://atcoder.jp/contests/abc224/tasks/abc224_a
# 提出AC
# https://atcoder.jp/contests/abc224/submissions/27562928

s = input()
if s[len(s)-1] == "r":
  ans = "er"
elif s[len(s)-1] == "t":
  ans = "ist"

print(ans)