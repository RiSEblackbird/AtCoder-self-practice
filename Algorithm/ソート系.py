##### bisect --- 配列二分法アルゴリズム
# https://docs.python.org/ja/3/library/bisect.html#module-bisect

# 例 各メンバーの戦闘力<- 戦闘力4の新人は序列何人目になるか
import bisect
N = [12,10,8,6,4,2]
print(N, bisect.bisect_left(N,9) )
N.sort()
print(N, bisect.bisect_left(N,9) )
# 専らソート済みの配列に使用するもの
# [12, 10, 8, 6, 4, 2] 6
# [2, 4, 6, 8, 10, 12] 4
