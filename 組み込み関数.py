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

### 配列要素を反転 reversed()
# https://docs.python.org/ja/3/library/functions.html#reversed
b = ["a", "b", "c"]
print( reversed(b) ) # <list_reverseiterator object at 0x7f2a096f95e0>
print( *reversed(b) ) # c b a
print( [*reversed(b)] ) # ['c', 'b', 'a']
print( "".join(reversed(b)) ) # cba
