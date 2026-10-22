# remove function hard code logic

# this is example 

# list = [1,2,3,4,5,6]
# list.remove(5)
# print(list)

# 1st Approach

list = [1,2,3,4,5,6]

blnk_list = []
for i in list:
    if i !=5:
        blnk_list = blnk_list + [i]
print(blnk_list)