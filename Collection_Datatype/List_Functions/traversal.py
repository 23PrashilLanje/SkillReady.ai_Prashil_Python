# list traversal

num = [10,20,30,40]
for i in num:
    print(i)

# here your output should be only (value)
#  10
#  20
#  30
#  40


for i in range(len(num)):
    print(i,num[i])

# here your output should be both (index and value)
# 0 10
# 1 20
# 2 30
# 3 40