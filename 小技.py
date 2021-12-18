##### 短縮構文

### "YNeos", "NYoe s"
# 全部そう
A = [1,1,1]
print( "NYoe s"[ all(a + 2 == 3 for a in A)::2] )
# 一つはそう
print( "NYoe s"[ any(a + 2 == 3 for a in A)::2] )
