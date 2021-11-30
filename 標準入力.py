##### 標準入力 #####
# 下記リンクや提出サンプルなどから
#   競プロ等におけるpython3の標準入力
#   https://qiita.com/zenrshon/items/c4f3849552348b3dbe67

### 一行の文字列の分解
s = list(input())
print(s)
# abc
# ['a', 'b', 'c']

n,k,a = map(int, input().split())
print("n={}, k={}, a={}".format(n,k,a))
# 3432 85 564
# n=3432, k=85, a=564


# N
# A11 A12 A13
# .
# AN1 AN2 AN3
###
# 3
# 123 423 654
# 234 547 479
# 294 472 692
N = int(input())
s = [input().split() for _ in range(N)]
print(s)
# [['123', '423', '654'], ['234', '547', '479'], ['294', '472', '692']]


## 文字列の分解
# A B
# 54538 25345
a, b = map(str, input().split(" "))
a_list = list(a)
b_list = list(b)
print(a_list)
print(b_list)
# ['5', '4', '5', '3', '8']
# ['2', '5', '3', '4', '5']