# 1st Approach

# list = [1,2,3,4]
# list = list + [5]
# print(list)


# 2nd Approach

# list = [1,2,3,4]
# for i in range(5):
#     if i<len(list):
#         print(list[i])
#     else:
#         list = list + [5]
# print("using for loop",list)

# 3rd approach 

# list1 = [1,2,3,4]
# list1.insert(4,5)
# print("using insert",list1)


# 4th approach 

# list2 = [1,2,3,4,5,6]
# blank_list = []
# for i in list2:
#     blank_list = blank_list + [i]
# blank_list = blank_list + [7]
# print(blank_list)

# 5th Approach using user input

# number = []
# for i in range(3):
#     add = int(input("Enter a Number:"))
#     number = number + [add]
# print(number)