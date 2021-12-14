# B - Many Oranges https://atcoder.jp/contests/abc195/tasks/abc195_b
# 
A,B,W = map(int, input().split())
min = 1000*W/A
max = 1000*W/B
if min > max:
  print("UNSATISFIABLE")
else:
  print(min, max)

# 1 <= A <= B <= 1000
# 1<= W <= 1000
# ->: AN <= 1000W <= BN
# ->: N <= 1000W/A, 1000W/B <= N

# 解答、解説で理解できず、後日
