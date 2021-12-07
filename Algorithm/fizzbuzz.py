# x = int(input())
x = 0

while x < 101:
  if (x % 3 == 0) and (x % 5 == 0):
    ans = "FizzBuzz"
  elif x % 3 == 0:
    ans = "Fizz"
  elif x % 5 == 0:
    ans = "Buzz"
  else:
    ans = "NO"

  print("{}:{}".format(x, ans))
  x += 1

#   $ python3 fizzbuzz.py
# 0:FizzBuzz
# 1:NO
# 2:NO
# 3:Fizz
# 4:NO
# 5:Buzz
# 6:Fizz
# 7:NO
# 8:NO
# 9:Fizz
# 10:Buzz
# 11:NO
# 12:Fizz
# 13:NO
# 14:NO
# 15:FizzBuzz
# 16:NO
# 17:NO
# 18:Fizz
# 19:NO
# 20:Buzz
# 21:Fizz
# 22:NO
# 23:NO
# 24:Fizz
# 25:Buzz
# 26:NO
# 27:Fizz
# 28:NO
# 29:NO
# 30:FizzBuzz
# 31:NO
# 32:NO
# 33:Fizz
# 34:NO
# 35:Buzz
# 36:Fizz
# 37:NO
# 38:NO
# 39:Fizz
# 40:Buzz
# 41:NO
# 42:Fizz
# 43:NO
# 44:NO
# 45:FizzBuzz
# 46:NO
# 47:NO
# 48:Fizz
# 49:NO
# 50:Buzz
# 51:Fizz
# 52:NO
# 53:NO
# 54:Fizz
# 55:Buzz
# 56:NO
# 57:Fizz
# 58:NO
# 59:NO
# 60:FizzBuzz
# 61:NO
# 62:NO
# 63:Fizz
# 64:NO
# 65:Buzz
# 66:Fizz
# 67:NO
# 68:NO
# 69:Fizz
# 70:Buzz
# 71:NO
# 72:Fizz
# 73:NO
# 74:NO
# 75:FizzBuzz
# 76:NO
# 77:NO
# 78:Fizz
# 79:NO
# 80:Buzz
# 81:Fizz
# 82:NO
# 83:NO
# 84:Fizz
# 85:Buzz
# 86:NO
# 87:Fizz
# 88:NO
# 89:NO
# 90:FizzBuzz
# 91:NO
# 92:NO
# 93:Fizz
# 94:NO
# 95:Buzz
# 96:Fizz
# 97:NO
# 98:NO
# 99:Fizz
# 100:Buzz