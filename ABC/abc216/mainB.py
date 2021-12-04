# B - Same Name
# https://atcoder.jp/contests/abc216/tasks/abc216_b
# 提出AC
# https://atcoder.jp/contests/abc216/submissions/27692538
N = int(input())
ST = {input() for _ in range(N)}
print( "Yes" if len(ST) < N else "No" )

### 解説読んだうえでメモ
# 同姓同名を調べるのであれば、苗字と名前を分ける必要がない。
# N行分を配列で取得し、set型のオブジェクトに変換して、
# 人数Nより小さくなれば、同姓同名が１組以上存在することを意味する。
