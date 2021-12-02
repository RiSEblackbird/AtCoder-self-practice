# range() 関数
# https://docs.python.org/ja/3/tutorial/controlflow.html#the-range-function
# 0～(引数-1) まで {引数}回ループ

### 行と列の入れ替え
a_list = [1,2,3,4,5]
b_list = [531453,846542,368246,935653,354562]
print(a_list)
print(b_list)

for (a, b) in zip(a_list, b_list):
  print([a,b])

# [1, 531453]
# [2, 846542]
# [3, 368246]
# [4, 935653]
# [5, 354562]

C = []
for i in range(5):
    C.append((a_list[i],b_list[i]))

print(C)
# [(1, 531453), (2, 846542), (3, 368246), (4, 935653), (5, 354562)]

C = sorted(C)[::-1]
print(C)
# [(5, 354562), (4, 935653), (3, 368246), (2, 846542), (1, 531453)]

### 文字送り
s = input()
a = [s[i:]+s[:i] for i in range(len(s))]
print(a)
# abc
# ['abc', 'bca', 'cab']

# 試作（上記を使うこと）
S = list(str(input()))
words = ["".join(S)]

for i in range(len(S)-1):
  temp_list = []
  for j in range(len(S)-1):
    temp_list.append(S[j+1])
  temp_list.append(S[0])
  words.append("".join(temp_list))
  S = temp_list

print(words)
# abcd
# ['abcd', 'bcda', 'cdab', 'dabc']
