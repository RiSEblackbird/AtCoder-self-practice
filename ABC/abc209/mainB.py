# B - Can you buy them all? https://atcoder.jp/contests/abc209/tasks/abc209_b
# 提出AC https://atcoder.jp/contests/abc209/submissions/27729002
N,X = map(int, input().split())
A = list(map(int, input().split()))

print( "Yes" if X >= (sum(A) - N//2) else "No" )

# 偶数番目、すなわち
# 奇数インデックスの要素を足すたびに1円引かれるので、(N//2)円だけ値引きされる。
# ループの回数は100回が上限なので、条件で途中で切らずにすべて回してしまえばいい。
