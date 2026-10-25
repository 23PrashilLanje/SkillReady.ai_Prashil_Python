# starting date 24 oct 2026

### creating tuples  ###

# a  = (10,20,30)

# # WITHOUT PARENTHESIS
# b = 10 ,20, 30

# # EMPTY TUPLE
# c = ()

# # ONETIME TUPLE
# d = (5,)

# # FROM A LIST
# e = tuple([1,2,3])

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


## 4th slide ACCESSING TUPLE ITEMS  ###

# colors = ("red" , "green" , "blue" , "black")
# print(colors[0])   # red
# print(colors[2])   # blue
# print(colors[-1])  # black
# print(colors[-2])  # blue


## 5th TUPLE SLICING   ###

# nums = (10, 20, 30, 40, 50, 60)
 
# print(nums[1:4])    # (20, 30, 40)
# print(nums[:3])     # (10, 20, 30)
# print(nums[3:])     # (40, 50, 60)
# print(nums[::2])    # (10, 30, 50)  step jumps
# print(nums[::-1])   # (60, 50, 40, 30, 20, 10)  REVERSED


## 6th TUPLE IMMUTABILITY   ###

# numbers = (10, 20, 30)
 
# # This would raise TypeError:
# # numbers[1] = 99
 
# # Create a new tuple instead
# numbers = numbers[:1] + (99,) + numbers[2:]
# print(numbers)



## 7th Built-in Tuple Methods  ###

# values = (10, 20, 10, 30, 10)
 
# print(values.count(10))      # 3
# print(values.index(20))      # 1
# print(values.index(10, 1))   # 2 "ky 10 1st index pe hai>> so nhi wo  2  index pe hai"


## 8th . Useful Built-in Functions  ###

values = (8, 3, 12, 5)
 
print(len(values))        # 4
print(min(values))        # 3
print(max(values))        # 12 
print(sum(values))        # 28 all items addition
print(sorted(values))     # [3, 5, 8, 12] sorting
