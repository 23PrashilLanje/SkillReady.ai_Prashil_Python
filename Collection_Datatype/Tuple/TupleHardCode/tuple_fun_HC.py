
# suppose ypu have data which contain some duplicate element and you have to find which is duplicate

# data = (10,20,10,30,10)

# # # for this built in function is count()
# print(data.count(10))  # 3


## MANUAL LOGIC  HARD CODE OF THIS  ##

data = (10,20,10,30,10,10)

count = 0
for i in data:
    if i == 10:
        print("manual logic: ",i)
        count += 1
print(count, "times") # 4