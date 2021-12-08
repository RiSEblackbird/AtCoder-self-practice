# B - Visibility https://atcoder.jp/contests/abc197/tasks/abc197_b
# 
H,W,X,Y = map(int, input().split())
S = list( input() for _ in range(H) )

count = 1
for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
  i = 1
  while S[X-1 + i*d[0]][Y-1 + i*d[1]] == "." and 0 <= (X-1 + i*d[0]) <= (W-1) and 0 <= (Y-1 + i*d[1]) <= (H-1):
    print((X-1 + i*d[0]),(Y-1 + i*d[1]))
    count += 1
    i += 1
print(count)

# 碁盤


# 後日