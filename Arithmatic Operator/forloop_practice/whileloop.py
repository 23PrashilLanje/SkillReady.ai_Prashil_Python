# while loop practice

# count = 2
# while count<= 5:
#     print("i lv u")
#     count+=1
# print(count) # >> 6 

# i = 1
# while i<= 5:
#     print("alka",i)
#     i += 1

# i = 5
# while i>=0:
#     print(i)
#     i -= 1

# que 1 [print number from 1 to 100]

# num = 1
# while num <= 100:  # this is STOP condition
#     print(num)
#     num += 1
# print("loop End")


# que 2 [print number from 100 to 1]

# num = 100
# while num >= 1: # STOP condition
#     print(num)
#     num -= 1
# print("loop End")


# que 3 [print multiplication table of 3 user input]

# n = int(input("which number table want to print please enter:"))
# num = 1
# while num <=10:
#     print(n * num)
#     num += 1


# que 4  print elements of following list  using a loop (SQ of 1 to 10)

# num= [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

# que 5 search a number x in this tuple using loop

num1= (1,4,9,16,25,36,49,64,81,100)  # this is tuple

i = 0
while i< len(num1):
    print(num1[i])
    i += 1

# print num from 1 to 5 while loop 

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# EXAMPLE >> TIMER FROM YOUTUBE FROM PYTHON CODING (CLCODING)

# import time
# count = 10

# while count > 0:
#     print(count)
#     time.sleep(1) # perform in seconds
#     count -= 1
# print(" times up!")


# EXAMPLE OF LOGIN ATTEMPTS AND PASSWORD SUCCESSFULL

# attempt = 0
# max_attempts  = 3

# while attempt < max_attempts:
#     password = input("enter password:")

#     if password == "prashil123":
#         print("login approved")
#         break

#     attempt += 1
#     print("incorrect password : ")
# print(" login process end:")