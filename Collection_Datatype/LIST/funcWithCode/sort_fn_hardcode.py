# sort function hardcode logic

# this is example

list = [5,8,7,6,1,3,2,4]
b =list.sort()
print(list)

# 1st Approach

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
            list[i],list[j] = list[j],list[i]
print(list)



# 2nd Approach

list = [5,8,7,6,1,3,2,4]

for i in range(len(list)):
    for j in range(i + 1,len(list)):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)