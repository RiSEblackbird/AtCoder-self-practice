a, b = map(str, input().split(" "))
a_list = list(a)
b_list = list(b)

if len(a_list) > len(b_list):
  for i in range( len(a_list) - len(b_list) ):
    b_list.insert(0, "0")
elif len(a_list) < len(b_list):
  for i in range( len(b_list) - len(a_list) ):
    a_list.insert(0, "0")

ans = "Easy"
i = 0
while i < len(a_list):
  add = int(a_list[i]) + int(b_list[i])
  if add >= 10:
    ans = "Hard"
    break

  i += 1

print(ans)

# print("{},{}".format(a_list, b_list) )