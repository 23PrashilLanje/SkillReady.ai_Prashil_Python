### Python List Programming Tasks word file on python folder ###



# list = [10,20,30,40]
# list2 = [30,40,50,10]
# for i in range (len(list)):
#     for j in range (len(list2)):
#         if list[i]== list2[j]:
#             print(list[i],end=" ")
#    # print(i,end=" ")
     

# this operation without using range

# for i in list:
#     for j in list2:
#         if i==j:
#             print(i)





list2=[2,3,4,7,8,1]
#find the any two elements which sum is 10 7+3=10
#2+8=10

for i in list2:
    for j in list2:
        if i + j == 10:
            print(i ,j , "=", "10")