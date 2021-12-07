# B - Intersection https://atcoder.jp/contests/abc199/tasks/abc199_b
# 提出AC https://atcoder.jp/contests/abc199/submissions/27757618
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
span = min(B) - max(A) + 1
print(span if span > 0 else 0)

# {min(B)=6} <= x <= {max(A)=7}
# 差は 1 なので幅は 2 = 1 + 1
