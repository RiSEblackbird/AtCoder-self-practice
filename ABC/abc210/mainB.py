# B - Bouzu Mekuri https://atcoder.jp/contests/abc210/tasks/abc210_b
# 提出AC https://atcoder.jp/contests/abc210/submissions/27709502
N = int(input())
S = input()

print("Takahashi" if S.find("1") % 2 == 0 else "Aoki")

# 偶数0,2,4... Takahashi kun
# 奇数1,3,5.... Aoki kun
# N使わなかった

# 部分文字列 マッチ find()
