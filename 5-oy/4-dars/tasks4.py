# Task 4

# def func(param1:str,param2:str):
#     vowels = 'aeiou'
#     vowels_1 = []
#     vowels_2 =[]

#     for i in param1.lower():
#         if i in vowels and i not in vowels_1:
#             vowels_1.append(i)
    
#     for i in param2.lower():
#         if i in vowels and i not in vowels_2:
#             vowels_2.append(i)
    
#     for i in vowels_1:
#         if i not in vowels_2:
#             return False
#     return False

# second way

# def func(param1: str, param2: str):
#     vowels = set('aeiou')
#     vowels_1 = set(param1.lower()).intersection(vowels)
#     vowels_2 = set(param2.lower()).intersection(vowels)

#     return vowels_1 == vowels_2


# print(func('Assalomu alaykuim','Va alykum assalom'))
