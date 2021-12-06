# B - 180° https://atcoder.jp/contests/abc202/tasks/abc202_b
# 提出AC https://atcoder.jp/contests/abc202/submissions/27743858
S = input()
print( S.replace("6", "s").replace("9", "6").replace("s", "9")[::-1] )
# チェーンした処理を順次進めるので、互いに干渉しないようにする


# 問題の意味がわかっていなかった。文章を無視してた。
# 図形的に 180度 回転したものにならなければならない。
# ここまでテストサンプルも通っていないことになるが、字が小さくて気づけなかった。

# WA ↓とまったく同じ落ち方をした。
S = list(input())
print( "".join(reversed(S)) )


# WA テストケースが大量堕ち https://atcoder.jp/contests/abc202/submissions/27743658
# reversed() を知る前に勢いで書いた
S = list(input())
ans_list = []
for i in range(len(S)):
  ans_list.append(S[-(i+1)])
print( "".join(ans_list) )

# 文字列 入れ替え 反転
