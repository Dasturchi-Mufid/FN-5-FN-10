# 1) shuunday funksiya yozingki, u ikkita parametreni qabul qilsin birinchi parametredagi barcha sozlar 
# ikkinchi parametrea bo`lishi kerak. 
# 2) shunday funksiya yozingki u bittra parametrani str typda qabul qilsin va osha sozni ichidagi uli harflar sonini qaytarsin 
# 3)shunday funksiya yozingki u ichida raqamlarni qabul qilsin va 0llar sonini qaytarsin 
# 4) shunday funksiya yozingki u ikkita parametr qabul qilsin va 
# birinchi parametralarni ichidagi barcha unli harflar ikkinchisida mavjudligini tekshiring 
# """barcha natijalar githubga yuklanib reponi linkini yuboring"""

# Task 1

# def func(data1:str,data2:str):
#     splitting = data1.lower().split()
#     for i in splitting:
#         if i not in data2.lower():
#             return False
#     return True

# print(func('Assalomu alaykum','aSsalomu alaykum'))


# Task 2


# def func(param:str):
#     count = 0
#     vowels = 'aeiou'
#     for i in param.lower():
#         if i in vowels:
#             count += 1
#             print(i)
#             print(count)
#     return count

# print(func('Assalomu alaykum'))

# Task 3

# def func(*args):
#     count = 0
#     for i in args:
#         if i == 0:
#             count += 1
#     return count

# print(func(1,2,4,0,7,0,5,0,'salom'))

