##### 組み込み型 #####
# https://docs.python.org/ja/3/library/stdtypes.html?highlight=str%20replace#built-in-types
# > 主要な組み込み型は、数値、シーケンス、マッピング、クラス、インスタンス、および例外です。

### 二進数でのビットの長さ bit_length()
# https://docs.python.org/ja/3.8/library/stdtypes.html?highlight=bit#int.bit_length
print((3).bit_length())
# 2
# !!! 2の乗数を求める場合は, " (n).bit_length() - 1 "

### 要素の入れ替え str.replace(old, new[, count])
# https://docs.python.org/ja/3/library/stdtypes.html?highlight=str%20replace#str.replace
