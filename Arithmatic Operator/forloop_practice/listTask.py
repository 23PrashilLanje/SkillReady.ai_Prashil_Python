# Task 7: Check Whether a List Contains Duplicates

# nuumber= [10,20,30,40,20]

# duplicate = False

# for i in range(len(nuumber)):
#     for j in range(i + 1,(len(nuumber))):
#         if nuumber[i] == nuumber[j]:
#             print("duplicate found:", nuumber)
#             duplicate = True
#             break
#     if duplicate:
#         break
# if not duplicate:
#     print("no duplicate found")



 # Task 8: Find the First Duplicate Element

# numbers1 = [10, 20, 30, 40, 20, 50, 10]

# for i in range (len(numbers1)):
#     for j in range(i + 1,len(numbers1)):
#         if numbers1[i] == numbers1[j]:
#             print("frist duplicate element:",numbers1[i])
#             break
#     else:
#         continue
#     break


# sir code for task 8

# number = [10, 20, 30, 40, 20, 50]

# visible =[]
# for i in number:
#     if i in visible:
#         print(i)
#         break
#     visible.append(i)

# iss code ka output 20 hai..
#   

# Task 9: Find Unique Elements

numbers = [10, 20, 30, 20, 40, 10, 50]  # 30 40 50 aana chahiye

for i in range(len(numbers)):
    unique = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            unique = unique + 1

    if unique == 1:
        print(numbers[i])



# Task 10: Find Repeated Elements and Their Frequency

numbers1 = [10, 20, 10, 30, 20, 10, 40, 30]