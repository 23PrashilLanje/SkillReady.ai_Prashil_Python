 ## SET INTRODUCTION & PRACTICE  ##

# number = {1,2,3,4,5}
# print(type(number))
# print(len(number))

# numbers = {2, 2, 4, 6, 6, 8}
# # print(set(numbers))
# numbers.remove(8)
# print(numbers)

# fruits = {"apple", "mango"}

# fruits.add("banana")
# fruits.add("apple")

# print(fruits)


# fruits = {"apple", "mango", "banana"}

# fruits.pop()

# print(fruits)
# output >> kuch bhi not fix {'apple', 'banana'}


# numbers = {10, 20, 30}
# numbers.clear()
# print(numbers)

# Que > How can you check how many items are in a set?

# numbers = {10, 20, 30, 40, 50}
# print(len(numbers))  # 5

# fruits = {"apple", "mango", "apple", "banana"}
# print(len(fruits)) # 3


# numbers = {10, 20, 30, 40}
# print(20 in numbers)
# print(50 in numbers)

### union() in set ###

# a = {1,2,3}
# b = {3,4,5}
# c = {5,6,7}
# print(a.union(b)) # {1, 2, 3, 4, 5}
# print(a.union(b,c))
# # {1, 2, 3, 4, 5, 6, 7} not allow duplicate

### intersection() in set ###

# a = {1,2,3}
# b = {3,4,5}
# print(a.intersection(b))
# #  output {3}

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a.intersection(b))
# #  output {3,4}

### difference() in set ###

a = {1,2,3,4}
b = {3,4,5,6}
print(a.difference(b))
# output > {1,2}

# reverse the difference
print(b.difference(a))
# output > {5,6}

