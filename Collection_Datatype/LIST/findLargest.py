
# Find the Largest Element

numbers = [25, 10, 75, 40, 90, 15]

largest= 0
for i in numbers:
    if i> largest:  # 0>25= false  25>0= true
        largest = i
print(largest)


# Find the second  Largest Element by sir


secondlargest=[0]
for i in numbers:
    if  secondlargest and i!=largest:
        secondlargest = i
print("second largest number: ",secondlargest)




# Find the second  Largest Element mera waala

# numbers = [10, 50, 30, 80, 40]

# largest = numbers[0] 
# second_largest= numbers[0]

# for i in numbers:
#     if i > largest:
#         second_largest = largest
#         largest = i
#         # second_largest = i
# print(second_largest)
# print(largest)







# Find the smallest element

# numbers = [25, 10, 75, 40, 90, 15]

# smallest=  numbers[0]
# for i in numbers:
#     if i< smallest:  # 0>25= false  25>0= true
#         smallest = i
# print(smallest)






