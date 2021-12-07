# B - Do you know the second highest mountain? https://atcoder.jp/contests/abc201/tasks/abc201_b
# 提出AC https://atcoder.jp/contests/abc201/submissions/27756873
N = int(input())
ST = [ input().split() for _ in range(N) ]
TS = sorted(ST, key=lambda x: int(x[1]), reverse=True)
print(TS[1][0])

# lambda式 https://qiita.com/n10432/items/e0315979286ea9121d57
