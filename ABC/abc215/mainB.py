# B - log2(N) 
# https://atcoder.jp/contests/abc215/tasks/abc215_b
# 提出AC
# https://atcoder.jp/contests/abc215/submissions/27697487
print( (int(input())).bit_length()-1 )

### memo
# "N は 1≤N≤10^18を満たす整数である"
# とあるとおり、最小値は 2^0 <= N = 1
# bit長さでいうとN=8は「1000」で4, 一方で2^kのk=3
#                N=4は「100」で3,  一方で2^kのk=1
# つまり2^k を満たす k はビット長さから1を引いたものになる。

(1).bit_length

# WA
import math
print( math.floor(math.log2(int(input()))) )

# 指数 対数 math.log2() ビット数 bit_length()
