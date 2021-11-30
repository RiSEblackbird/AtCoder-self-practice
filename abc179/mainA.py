# A - Plural Form
# https://atcoder.jp/contests/abc179/tasks/abc179_a
# 提出AC
# https://atcoder.jp/contests/abc179/submissions/27608187
s = list(input())
if s[-1] == "s":
  s.append("es")
else:
  s.append("s")

print("".join(s))

# 結合 join() 追加 append()
