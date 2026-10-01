# # # data types 
# # # 1. List
# # # 2. Tuple
# # # 3. Set
# # # 4. Dictionary


# # # append.py

# # number = [1, 2, 3, 4, 5 ,6,7,8,9, 10]
# # number.append(11)
# # print(number)

# # #extend.py

# # a=[1, 2, 3, 4, 5]
# # b=[6, 7, 8, 9, 10]
# # a.extend(b)
# # print(a)



# #list_slicing.py

# list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list[1:7]) # slicing[staring index: ending index]

# #by default starting index is 0 and ending index is length of list


# print(list[-1]) # negative indexing
# print(list[-2]) # negative indexing
# print(list[-3]) # negative indexing

# print(list[-1:-7:-1]) # negative slicing #-1-1==>-2-1==>-3


# #reverse

# print(list[::-1]) # reverse the list


# sorting

# list1=[7,5,4,3,2,8,9,1,2,3,6]
# list1.sort() # sort the list in ascending order
# print(list1)

# list1.sort(reverse=True) # sort the list in descending order
# print(list1)    


# sorted function.py

# list=[30,10,20,]
# new_list=sorted(list) # sorted function will return a new list

# list1=list.sort() # sort method will change the original list
# print(new_list)
# print(list1) # original list will not be changed
# #create and return a sorted list sorteed()
# print(new_list) # original list will not be changed
# print(list) # original list will be changed



#traversing_list.py


# for loop & while loop can be used to traverse the list

# list=[1,2,3,4,5,6,7,8,9,10]
# print(list)
# for i in list:  # 1 2 3 ....last index tak data dega
#     print(i) # traversing the list using for loop



# new file list_with_user_input.py

# example for checking even and odd number using list with user input...



numbers=[]
for i in range(10):
    n=int(input("Enter a number: "))
    numbers.append(n)

    if n % 2 == 0:
        print(n,"your number is Even number")
    else:
        print(n," your number is Odd number")


print(numbers)



# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("your number is Even number")
# else:
#     print(" your number isOdd number")


