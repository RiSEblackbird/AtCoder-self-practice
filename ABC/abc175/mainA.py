# A - Rainy Season
# https://atcoder.jp/contests/abc175/tasks/abc175_a
# 提出AC
# https://atcoder.jp/contests/abc175/submissions/27608531
s = list(input())
if len(set(s)) == 1:
  ans = 3 if s[0] == "R" else 0
elif s[0] == s[1]:
  ans = 2 if s[0] == "R" else 1
elif s[1] == s[2]:
  ans = 2 if s[1] == "R" else 1
else:
  ans = 1

print(ans)

# MEMO : else で締めるの忘れがち。
# 　　　　テストケースでカバーされなければ提出してしまうところだった。

# 連続文字列
