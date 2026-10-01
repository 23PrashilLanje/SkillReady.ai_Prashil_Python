list=[1,2,3,4,5,6,7,8]

# [ 0 1 2 3 4 5 6 7 8]
# [      -4  -3  -2  -1]


print(list[0:5:2]) # [1, 3, 5]
print(list[0:5]) # [1, 2, 3, 4, 5]
print(list[3:5]) # [4, 5]

print(type(list))  # <class 'list'>

print(list[::-1]) #reverse [8, 7, 6, 5, 4, 3, 2, 1]

print(list[::-2]) # [8, 6, 4, 2] jump steps
