# C - X drawing
# https://atcoder.jp/contests/abc230/tasks/abc230_c
# 
# 

# WA
n,a,b = map(int, input().split())
p,q,r,s = map(int, input().split())

lines = [list("".join(".") for _ in range(n)) for _ in range(n)]

# 操作1
bottom = max(1-a, 1-b)
upper = min(n-a,n-b)

for i in range(upper-bottom):
  k = bottom + i
  lines[a+k-1][b+k-1] = "#"

# 操作2
bottom = max(1-a, b-n)
upper = min(n-a,b-1)

for j in range(upper-bottom):
  k = bottom + j
  lines[a+k-1][b-k-1] = "#"

for e in range(q-p+1):
  print("".join(lines[e][:s-r+1]))


  ################
