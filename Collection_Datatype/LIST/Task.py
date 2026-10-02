# new task 
#

# list = []

# user input leke data add krna hai 16 values
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# square => 2 sq =>4
#3 sq = 9
#4 sq = 16 no value
# addition task 
# if equal number addition => list
# 2+2=4  3+3 = 6  5+5=10 

# square = []
#equal no _add=[]


###############################################################


#TASK 


list = []
for i in range(1, 17):
    n= int(input("Enter Values IN list:"))
    list = list + [n]
#print(list)



# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for i in range(1,n):
    list.append(i)

square_list=[]
Addition_list=[]

for i in list:
    square = i * i

    if square in list:
        square_list.append(square)

    addition = i + 1    

    if addition in list:
        Addition_list.append(addition)

    print("MAin list:", list)
    print("square list:",square_list)
    print("Addition list:",Addition_list)