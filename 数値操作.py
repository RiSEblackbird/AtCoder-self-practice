##### 組み込み関数 #####
# https://docs.python.org/ja/3/library/functions.html

### 絶対値 abs()
# https://docs.python.org/ja/3/library/functions.html#abs

### 総和 sum()
# https://docs.python.org/ja/3/library/functions.html?highlight=sum#sum

### 整数型 int()
# https://docs.python.org/ja/3/library/functions.html#int
# 進数の変換もできる 
s = str(input())
print(int(s, 2)) # 第一引数は文字列型であることに注意！
# 11
# 3

### 二進数でのビットの長さ bit_length()
# https://docs.python.org/ja/3.8/library/stdtypes.html?highlight=bit#int.bit_length
print((3).bit_length())
# 2
# !!! 2の乗数を求める場合は, " (n).bit_length() - 1 "
