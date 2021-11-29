# A - Very Very Primitive Game
# https://atcoder.jp/contests/abc190/tasks/abc190_a
# 提出AC
# https://atcoder.jp/contests/abc190/submissions/27595557

a,b,c = map(int, input().split())
if a == b:
  ans = "Takahashi" if c == 1 else "Aoki"
elif a - b > 0:
  ans = "Takahashi"
elif a - b < 0:
  ans = "Aoki"
print(ans)

# 変にややこしいことしようとしてかえって混乱した
# print("a-dif={}, b-dif={}, c={}".format(a-dif,b-dif,c))
## [WA]
# a,b,c = map(int, input().split())
# dif = abs(a - b)
# if a == b:
#   ans = "Takahashi" if c == 1 else "Aoki"
# elif c == 0:
#   ans = "Takahashi" if a - dif > 0 else "Aoki"
# elif c == 1:
#   ans = "Aoki" if b - dif > 0 else "Takahashi"
# print(ans)
