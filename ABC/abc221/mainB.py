# B - typo
# https://atcoder.jp/contests/abc221/tasks/abc221_b
# 提出AC
# https://atcoder.jp/contests/abc221/submissions/27633014
[s,t] = [list(input()) for _ in range(2)]
ans = "No"
if s == t:
  ans = "Yes"
else:
  for i in range(len(s)-1):
    s[i], s[i+1] = s[i+1], s[i]
    if s == t:
      ans = "Yes"
      break
    s[i+1], s[i] = s[i], s[i+1]

print(ans)
# 並び替え部分の表現方法が思いつかず解説を見た

# 文字列 入れ替え 組み換え
