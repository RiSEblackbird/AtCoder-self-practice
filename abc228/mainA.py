s,t,x = map(int, input().split())
if s < t:
  ans = "Yes" if s <= x < t else "No"
else:
  ans = "No" if t <= x < s else "Yes"

print(ans)

# たぶんOK　https://atcoder.jp/contests/abc228/tasks/abc228_a
# taishi@DESKTOP-GIVL2DT:~/AtCoder$ python3 main.py
# 23 0 23
# Yes
# taishi@DESKTOP-GIVL2DT:~/AtCoder$ python3 main.py
# 7 20 12
# Yes
# taishi@DESKTOP-GIVL2DT:~/AtCoder$ python3 main.py
# 20 7 12
# No