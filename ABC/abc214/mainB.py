# B - How many? https://atcoder.jp/contests/abc214/tasks/abc214_b
# 提出AC https://atcoder.jp/contests/abc214/submissions/27698106
S,T = map(int, input().split())
print( sum((a+b+c<=S) * (a*b*c<=T) for a in range(101) for b in range(101) for c in range(101)) )

### memo
# 乗算による条件判定は式を()で囲んで式内の算術演算子を混同させないように注意。
