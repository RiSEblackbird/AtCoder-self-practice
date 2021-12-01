# A - ∴ (Therefore)
# https://atcoder.jp/contests/abc168/tasks/abc168_a
# 提出AC
# https://atcoder.jp/contests/abc168/submissions/27618837
N = list(input())
n = int(N[-1])
if len(set([2,4,5,7,9,n])) == 5:
  print("hon")
elif len(set([0,1,6,8,n])) == 4:
  print("pon")
else:
  print("bon")
