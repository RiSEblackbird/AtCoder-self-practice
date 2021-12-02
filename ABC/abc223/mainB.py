# B - String Shifting
# https://atcoder.jp/contests/abc223/tasks/abc223_b
# 提出AC　初見自力
# https://atcoder.jp/contests/abc223/submissions/27631571
S = list(str(input()))
words = ["".join(S)]

for i in range(len(S)-1):
  temp_list = []
  for j in range(len(S)-1):
    temp_list.append(S[j+1])
  temp_list.append(S[0])
  words.append("".join(temp_list))
  S = temp_list

words.sort()
print(words[0])
print(words[-1])
### 予めSを構成する文字列をソートして、最小の文字と最大の文字を取ってループ回数減らす工夫の予知ありそう。

# 辞書順 文字列 並び替え 組み換え
