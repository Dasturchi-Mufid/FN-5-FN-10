# Task 1

# def add_nums_list(list1,list2):
#     result1 = ''
#     result2 = ''

#     for i in list1:
#         result1 += str(i)

#     for i in list2:
#         result2 += str(i)
    
#     result = int(result1) + int(result2)

#     return result

# Task 2

# def add_nums_list(list1,list2):
#     result1 = ''
#     result2 = ''

#     for i in list1:
#         result1 += str(i)

#     for i in list2:
#         result2 += str(i)
    
#     result = int(result1) + int(result2)

#     return str(result)
    

# print(add_nums_list(list1=[1,2,45,9],list2=[1,2,4,5]))

# Task 3

# def check_palindrom(data:int):
#     num_str = str(data)
#     return num_str == num_str[::-1]

# print(check_palindrom(12.21))

# Task 4

# def checking(openn,closee):
#     check = {'(':')'}
#     return check[openn] == closee

# def check_bracket(data:str):
#     brackets = []

#     for i in data:
#         if i == '(':
#             brackets.append(i)
#         elif i == ')':
#             if not brackets or not brackets.pop() == i:
#                 return False

# data = '()()())('
# print(check_bracket(data=data))

# def check_bracket(data:str):
#     count = 0

#     for i in data:
#         if count < 0:
#             break
#         if i == '(':
#             count += 1
#         else:
#             count -= 1
#     return count == 0
# data = '()))()(())'
# print(check_bracket(data=data))

# a = 'sloom'
# a[1] = 'a' # bunday qilib bo`lmaydi
# print(a)

# a = 10
# b = a

# print(a == b)
# print(a is b)

import sys

a = '10'

print(a) # value
print(id(a)) # id
print(type(a)) # type
print(sys.getrefcount(a))
