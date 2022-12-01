### Control Flow
## 1. Conditional Statements
# if (True): "colon starts a block which is indented"
#   do this "everything which is indented comes into thhe block"
# elif (True):
#   do this
# else:
#   do this

a = True
if True:
    print(" true")
print("end")

if a:
    print(" true")
else:
    print("false")

b = 5
if b==3:
    print(" 3")
elif b==5:
    print("5")
else:
    print("not 3 or 5")

# x: int(-inf,inf)
# G -> x

# a = x<0
# b = x==0
# c = x>0

# a intersection b= b intersection c = a intersection c = phi



# q = Can A access profile B
# a = isFriend
# b = isBlocked
# c = isAdmin
# d = isMarkZuckerburg

# a b c d q
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 0
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1
# 1 0 0 0 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 0
# 1 1 0 1 1
# 1 1 1 0 0
# 1 1 1 1 1

# if _______:
#     print("has access")
# else:
#     print("access denied")