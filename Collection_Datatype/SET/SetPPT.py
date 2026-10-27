 ## SET INTRODUCTION & PRACTICE  ##

# number = {1,2,2,3,3,3}
# print((number))         # {1, 2, 3}
# print(len(number))      # 3

## Why Do We Need Sets? ##

# student = {'asha' , 'ravi' , 'asha' , 'neha'}
# unique_student = set(student)
# print(unique_student)
# print(len(unique_student))

# a = {}
# print(type(a))   # empty set declared dictionary type


# list = [10, 20, 10, 30, 20, 40]
# myset = set(list)
# print(myset)
# print(type(myset))
# print(len(list))


 ## 6th slide ##

# empty = set()
# from_list = set([1,2,2,3])
# from_text = set('hello')
# print(empty)            # set()
# print(from_list)        # {1, 2, 3}
# print(from_text)        # {'o', 'h', 'e', 'l'}

 ## 7th slide ##

# s = {10,20,20,30}
# print(len(s))       # 3
# s.add(40)
# print(40 in s)      # True
# # print(s[0])     # type error
# print(s)          # {40, 10, 20, 30}


 ## 8th slide  No Indexing OR Slicing ##

# s = {30,10,20}
# for i in s:
#     print(i)
# print(sorted(s))  # [10, 20, 30]


 ## 9th slide Membership and Length ##

# skills = {'python' , 'SQL' ,'java'}
# print('SQL' in skills)        # True
# print('c++' not in skills)    # True bcoz of not
# print(len(skills))             # 3


 ## 10th slide Adding One Element: add() ##

# skills ={'python' ,'SQL'}
# skills.add('power BI')
# skills.add('python')
# print(len(skills))      # 3

 ## 11th slide Adding Multiple Element: update() ##

skills ={'python' ,'SQL'}
skills.update(['java','SQL'])
skills.update(('git' , 'linux'))
print(skills)
print('c' in skills)  # False
print('java' in skills) # True
print(len(skills))

# o/p >> {'python', 'SQL', 'git', 'linux', 'java'} 