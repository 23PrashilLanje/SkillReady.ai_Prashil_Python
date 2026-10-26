### chatgpt practice code tuple chat  ###

# fruit = ("apple" , "banana" , "mango" ,)
# print(fruit)

# numbers = (10, 20, 30, 40, 50)
# print(numbers[3])

# numbers = (1, 2, 3, 4, 5)
# sum = 0
# for i in numbers:
#     sum = sum+i
# print("total of all items",sum)


# number = (10,20,30,40,)
# total = 0 
# for i in number:
#     total = total + i
# print(total)               # > 100



## find the largest number ###

# numbers = (12,45,7,89,23)
# largest = 0

# for i in numbers:
#     if i > largest:
#         largest  = i
# print(largest)
# print(numbers.index(largest))

## find the largest number with index position ###

# numbers = (12,45,7,89,23)
# largest = 0
# position = 0

# for i in range(len(numbers)):
#     if numbers[i] > largest:
#         largest = numbers[i]
#         position = i

# print("largest number" ,largest)
# print("position " , position )


## find the largest number with index position ###

numbers = (15, 62, 8, 91, 34, 50)

# print(max(numbers))
# print(numbers.index(91))

highest = 0
index = 0

for i in range(len(numbers)):
    if numbers[i] > highest:
        highest = numbers[i]
        index = i

print(highest)
print(index)