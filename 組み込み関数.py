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

### sorted(iterable, *, key=None, reverse=False)
# https://docs.python.org/ja/3/library/functions.html#sorted
b = ["d", "a", "b", "c"]
print( sorted(b) ) # ['a', 'b', 'c', 'd']

## lambda式を用いた方法
# 記事例：https://qiita.com/n10432/items/e0315979286ea9121d57
c = [["u", 3], ["m", 5], ["e", 1], ["s", 2], ["o", 4]]
c_desc1 = sorted(c, key=lambda x: int(x[1]), reverse=True)
c_desc2 = sorted(c, key=lambda x: -int(x[1]))
print(*list(c_desc1[i][0] for i in range(5)), sep="") # mouse
print(*list(c_desc2[i][0] for i in range(5)), sep="") # mouse
