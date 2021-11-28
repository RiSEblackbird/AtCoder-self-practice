# 問題よく読めてなかった。文字列は2文字以上ずっと続くと思い込んでた。
s = [input() for i in range(2)]

s1 = s[0]
s2 = s[1]

s1_flg = 1 # 1行目の詰みフラグ
s2_flg = 1 # 2行目の詰みフラグ
flg = 0 # 詰むフラグ

for i, item in enumerate(s1):
  if i == len(s1):
    break

  ss1 = [s1[i], s1[i+1]]
  ss2 = [s2[i], s2[i+1]]



  if ss1[0] == ".":
    if ss2[0] == "." or ss2[1] == ".":
      flg = 1
  elif ss1[0] == "#" and ss1[1] == ".":
    if ss2[0] == "." or ss2[1] == ".":
      flg = 1

  if [ss1[0], ss1[1]] != [".", "."]:
    s1_flg = 0

  if [ss2[0], ss2[1]] != [".", "."]:
    s2_flg = 0

# 最後にどちらか片方でも行が"."で詰まっていれば詰み
if s1_flg == 1 or s2_flg == 1:
  flg = 1

ans = "Yes" if flg == 0 else "No"
print(ans)


# 感想
# 最後２分。最初の行と最後の行が壁になっているだけならまだ詰みの条件ではない