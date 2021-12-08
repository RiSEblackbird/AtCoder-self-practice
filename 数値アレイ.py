##### array --- 効率のよい数値アレイ #####
### https://docs.python.org/ja/3/library/array.html?highlight=append

### array.append() アレイの末尾に要素を追加
# https://docs.python.org/ja/3/library/array.html?highlight=append#array.array.append
A = [1,2,3]
A.append(4)
print(A) # Aそのものを操作するので、処理単体で実行しないといけない。

### array.index() 引数の要素が何番目であるかを取得
# https://docs.python.org/ja/3/library/array.html?highlight=index#array.array.index
# 
# 注意：「何番目？」の問いだと 1 を足すこと。(リストの1番目は インデックス == 0 なので。)

### array.insert(i, x) 位置iの前に値xをもつ新しい要素を挿入
# https://docs.python.org/ja/3/library/array.html?highlight=index#array.array.insert
# 加算式の方が楽
