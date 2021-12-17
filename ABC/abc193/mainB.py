# B - Play Snuke https://atcoder.jp/contests/abc193/tasks/abc193_b
# 提出AC https://atcoder.jp/contests/abc193/submissions/27945326
### やったこと
## 店[i]での購入価格or(-1)を配列に格納、list(set())で重複なくしてソート、
## 最小が-1かつ唯一の要素なら-1を出力(どこでも買えなかった)
## 複数要素なら先頭が-1なら２番目、違えば１番目の価格を出力
N = int(input())
prices = [0]*N
for i in range(N):
  a, p, x = map(int, input().split())
  prices[i] = p if x - a > 0 else -1

prices = sorted(list(set(prices)))

if len(prices) == 1 and min(prices) == -1:
  print(-1)
else:
  print( prices[0] if prices[0] != -1 else prices[1] )

# ↓解答閲覧後の感想
# ループ内でアウトプットの値を更新する方針でよかった
# i回目の最小値が(-1) or (-1以上) なら更新する
# 提出分を改良してみる
# ボツ下記未完成破棄　ifがごちゃごちゃかえってややこしい　提出分↑のままでいい
N = int(input())

ans = -1
for i in range(N):
  a, p, x = map(int, input().split())
  if ans == -1:
    if x > a:
      ans = x - a
  else:
    if x - a < ans:
      ans = x - a

print(ans)
