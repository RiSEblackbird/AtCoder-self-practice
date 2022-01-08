# A - Weird Function https://atcoder.jp/contests/abc234/tasks/abc234_a
# AC https://atcoder.jp/contests/abc234/submissions/28390603
t = int(input())

def f(t):
  return t*t + 2*t + 3

print( f(f(f(t) + t) + f(f(t))) )