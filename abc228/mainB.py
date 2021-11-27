### problem https://atcoder.jp/contests/abc228/tasks/abc228_b
# https://atcoder.jp/contests/abc228/submissions/27508332
# から引用、提出しないこと
# 理解できなかった
N,S=map(int,input().split())
X=list(map(int,input().split()))
print("X:{}".format(X))
A=[False]*N
print("A[]:{}".format(A))
s=S
for i in range(N):
  if A[s-1]:
    break
  else:
    print("s:{}".format(s))
    A[s-1]=True
    print("今回A[]:{}".format(A))
    s=X[s-1]
count = A.count(True)
print(count)