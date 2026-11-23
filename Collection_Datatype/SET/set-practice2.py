# numbers = {10, 20, 30, 20, 40}
# print(numbers)

# a = {10, 20}
# a.add(30)
# a.update([40,50])
# print(a)


# a = {10, 20, 30}
# a.add(20)
# a.add(40)
# print(len(a))

# a = {10,20,30,40}
# a.remove(50)
# a.discard(40)
# a.pop()
# a.clear()
# print(a)

# a = {10,20,30}
# print(len(a))
# print(20 in a)
# print(50 not in a)

# a = {10,20,30}
# b = a.copy()
# print(b)

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))  # {1,2}
# print(a.symmetric_difference(b))


# a = {10,20}
# b = {10,20,30,40}

# # print(a.issubset(b))  #True
# # print(b.issubset(a))  #False

# print(b.issuperset(a))  #True
# print(a.isdisjoint(b))  #False DO A and B have NO common element


# a = {1, 2, 3}
# a.add(3)
# a.add(4)
# a.add(5)
# print(a)
# print(len(a))
# # {1, 2, 3, 4, 5} and 5

# a = {10,20,30,40,50}
# b = {30,40,60,70}

# x = a.difference(b)
# y = b.difference(a)
# z = a.intersection(b)
# print(x)
# print(y)
# print(z)
# print(len(x) + len(y) + len(z))


# a = {1,2,3,4}
# b = {3,4,5,6}

# a.update(b) # Add all elements of b into a. this print all non duplicate elemnt
# a.discard(3)

# result = a.difference(b)
# print(a)
# print(result)
# print(len(a))


# a = {2,4,6,8,10}
# b = {4,8,12,16}

# x = a.symmetric_difference(b)
# y = x.intersection(a)

# print(x)
# print(y)
# print(len(x) + len(y))


# a = {10,20,30}
# b = {10,20,30,40,50}

# print(a.issubset(b)) # True
# print(b.issuperset(a))  # True
# print(a.isdisjoint(b)) # False it check two set have zero common elements

a = {10, 20, 30}
b = {40, 50, 60}
c = {30, 40, 50}
print(a.isdisjoint(b))
print(a.isdisjoint(c))