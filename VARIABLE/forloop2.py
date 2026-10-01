
# DATE 22/ 9/ 2026 (7 PM )


# for i in range(0,11,2):    # 0 is starting point and 11 is ending point and 2 is increment value
#     print(i)


# for loop REVERSE operation
# isme loop ko batana padega ki value decrement hori hai 


# for i in range(11,0,-1):   # 11 is starting point and 0 is ending point and -1 is decrement value steps
#      print(i)


#EXAMPLE 

# for i in range(10,1,-2):  # output 10 8 6 4 2 
#      print(i)




# for i in range(5):
#     print(i)
# else:
#     print("loop completed")


    # example


# for i in range(1, 6):

#     if i == 3:
#         break

# else:
#     print("loop completed")
#         # OUTPUT OF THIS 
#         #1
#         #2  complete



        # exapmle



# for i in range(1, 6):
#        if i == 3:
#               continue

#        # continue value ko skip karega jaise ki i == 3, so 3 ko skip then print as usual.
#        print(i)



 # example

# for i in range(1,3):
#     for i in range(1,3):
#         print(i,j)

            #                   #output
            #                  # i = 1  j = 1
            #                  # i = 1  j = 2
            #                  # i = 2  j = 1
            #                  # i = 2  j = 2
                             



# DATE 23/09/2026




# for i in range(5):
#     print(i,end=" ")



    #  ADDITION OF ELEMENT

# addition = 0
# for i in range(1,6):
#         print(i,end=" ")
#         # additon = addition+i
#         addition += i
# print("addition = ", addition)





# QUESTION even cond check krni hai or odd num print hone chahiye

# agar != krte hai toh ODD numbers print ( 1  3  5  7  9 ) 
# agar == hrte hai toh EVEN numbers print ( 2  4  6  8  10  )


# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(i,end="   ")



  # EXAMPLE


# for  i in range(1,6):
#     print("*" * i)


# reversed this


# for i in range(5,0,-1):    
#     print("*" * i)


  # EXAMPLE square print


for i in range(5,0,-1):
    print("*" * i)
n = int(input("enter any number"))
for i in range(n):
     
    for j in range(n):
        
        print("*" , end=" ")
    print()



# 5*5 print output

# for i in range(5):
#     for j in range(5):
#         print("*", end= " ")
#     print()

