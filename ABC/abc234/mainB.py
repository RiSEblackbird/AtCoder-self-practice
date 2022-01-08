# B - Longest Segment https://atcoder.jp/contests/abc234/tasks/abc234_b
# https://atcoder.jp/contests/abc234/submissions/28407508
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

tmp = 0
for n in range(N-1):
  for i in range(n, N-1):
    dd = (XY[n][0] - XY[i+1][0])**2 + (XY[n][1] - XY[i+1][1])**2
    if tmp < dd:
      tmp = dd

print(round(tmp**0.5, 10))

  #####
      # print("({},{}),({},{})".format(XY[n][0],XY[n][1],XY[i+1][0],XY[i+1][1]))
    # print(dd)