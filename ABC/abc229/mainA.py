# A - First Grid
# https://atcoder.jp/contests/abc229/tasks/abc229_a
# 提出AC
# https://atcoder.jp/contests/abc229/submissions/27567759
S = [list(input()) for _ in range(2)]

if (S[0][1] == "." and S[1][0] == ".") or (S[0][0] == "." and S[1][1] == "."):
    print("No")
else:
    print("Yes")

# ###..##
# ..#####
# [['#', '#', '#', '.', '.', '#', '#'], ['.', '.', '#', '#', '#', '#', '#']]
# Yes