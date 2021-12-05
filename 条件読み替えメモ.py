### 与えられた4桁の数字がすべて同じ数字であること
num1, num2 = 7777, 7778
A, B = list(str(num1)), list(str(num2))
print(num1,num2)
print(A,B)
print( len(set(A)) == 1, len(set(B)) == 1 )
print( num1 % 1111 == 0, num2 % 1111 == 0 )
# 7777 7778
# ['7', '7', '7', '7'] ['7', '7', '7', '8']
# True False
# True False
