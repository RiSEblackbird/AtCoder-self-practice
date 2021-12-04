##### 4. その他の制御フローツール¶ #####
# https://docs.python.org/ja/3/tutorial/controlflow.html#more-control-flow-tools

### 4.8.5. 引数リストのアンパック
# https://docs.python.org/ja/3/tutorial/controlflow.html#tut-unpacking-arguments
#
# 配列要素を展開表示したいときいちいち回して要素出力しなくても*[List]でいける
A = [2,4,6] # 以下の2行の出力は同じ結果
print(A[0],A[1],A[2])
print(*A)
# 更にスペースを縮めて出力する場合はsep=""をつける
print(*A, sep="")
# 2 4 6
# 2 4 6
# 246
