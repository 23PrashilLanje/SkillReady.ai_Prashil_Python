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

# values = (8, 3, 12, 5)
 
# print(len(values))        # 4
# print(min(values))        # 3
# print(max(values))        # 12 
# print(sum(values))        # 28 all items addition
# print(sorted(values))     # [3, 5, 8, 12] sorting


## 9th . Joining and Repeating Tuples  ###

# a = (1, 2)
# b = (3, 4)
 
# print(a + b)        #(1, 2, 3, 4) 
# print(a * 3)        #(1, 2, 1, 2, 1, 2) 3 times print
# print(2 in b)       #False
# print(5 not in a)   #True


## 10th . 10. Iterating Through a Tuple  ###

# languages = ("Python", "Java", "C++")
 
# for i in languages:
#     print(i)
 
# for index, i in enumerate(languages):
#     print(index, i)

# enumerate me ek variable ki value 2 variable ko assign hogi esliye enumeerate use krte hai  

## 11th Tuple Packing and Unpacking  ###

# student = ("Maya", 20, "IT")  # packing
 
# name, age, branch = student  # unpacking
 
# print(name)     # Maya
# print(age)      # 20
# print(branch)   # IT


## 12th Starred Unpacking  ###

# values = (10, 20, 30, 40, 50)
 
# first, *middle, last = values
 
# print(first)    # 10 
# print(middle)   # [20, 30, 40]
# print(last)     # 50



## 13th Nested Tuples  ###

# records = (
#     ("Asha", 85),
#     ("Rohan", 92),
#     ("Neha", 78)
# )
 
# print(records[1])      # ('Rohan', 92)
# print(records[1][0])   # Rohan
# print(records[2][1])   # 78


## 14th  Tuple vs List  ###

# items_list = [10, 20, 30]
# items_tuple = (10, 20, 30)
 
# items_list[0] = 99
# # items_tuple[0] = 99  # TypeError not possible immutable
 
# print(items_list)    # [99, 20, 30]
# print(items_tuple)   # (10, 20, 30)


## 15th  A Tuple Can Contain a Mutable List  ###

# data = (1, [2, 3], 4)
 
# data[1].append(99)   # (1, [2, 3, 99], 4)
# print(data)
 
# # This fails:
# # data[1] = [5, 6]


## 16th  Converting Between Lists and Tuples  ###

t = (1,2,3)    # tuple type
lst = list(t)  # list type
lst.append(4)  

new_tuple = tuple(lst)

print(lst)          # [1, 2, 3, 4]
print(new_tuple)    # (1, 2, 3, 4)


### 17th  Sorting Tuples   ###


scores = (("Asha", 85), ("Rohan", 92), ("Neha", 78))
 
by_score = tuple(sorted(scores, key=lambda item: item[1]))
 
print(by_score)


### 18th Membership, any(), and all()   ###

values = (0,2,4,6)
print(4 in values)    # True
print(5 in values)    # False
print(any (values))   # True
print(all (values))  # False