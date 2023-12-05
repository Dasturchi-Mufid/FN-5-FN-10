# 1) bitta parametr list typeda qabul qiluvchi funksiya yozing. 
# o`sha listni ichida barcha elementlarni boshidagi umumiy joyii topuvchi dastur yozing. 
# agar listni ichidagi elementlar boshi boshqa elementlarda takrorlanmasa "" qaytaring.
# --- ['salom', 'salim', 'salkam']-> 'sal' ['salom', 'salim', 'alik'] -> ' ' ['salom', 'alik'] -> ' ' 
# 2) ikkita parametr qabul qiluvchi funksiya yozing. birinchi parametr str ikkinchisi int bo`lsin. 
# berilgan strni indexini intga ko`ra topuvchi dastur yozing. (index methoddan foydalanmang). 
# --- 'yaxshimisiz', 2-> x 'kompyuter', 5->u 
# 3) ikkita parametr qabul qiluvchi funksiya yozing. ikki parametr ham str bo`lsin, 
# birinchi elementni ichida ikkinchi element nechanchi index asosida turganini toping.
# --- 'yaxshimisiz', 'y'-> 0 'salom', 's' -> 0 
# 4) list typeni qabul qiluvchi fun yozing. uni har juft elementini teskari qilsin [1,2,3,4] [2,1,4,3] 
# 5) raqamlar matrixini hisoblovchi funskiay tuzing. [[1,2,3], [4,5,6], [7,8,9] -> [1,2,3,6,9,8,7,4,5]

# Task 1

# def find_common_prefix(words:list):
#     if not words:
#         return ""

#     prefix = words[0]
#     for word in words[1:]:
#         i = 0
#         while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
#             i += 1
#         prefix = prefix[:i]

#     return prefix


# print(find_common_prefix(['salom', 'salim', 'salkam']))
# print(find_common_prefix(['salom', 'salim', 'alik']))
# print(find_common_prefix(['salom', 'alik']))

# Task 2

# def find_char_at_index(txt:str, index:int):
#     if 0 <= index < len(txt):
#         return txt[index]
#     else:
#         return None

# Ustozni vazifasini boshqacha tushunib olgan bo`lishim mumkin. Shuning uchun ikkinchi variyantni qoldridim.

# def find_char_at_index_2(txt:str,index:int):
#     str_index = 0
#     for i in txt:
#         if str_index == index:
#             return i
#         str_index += 1


# print(find_char_at_index_2('yaxshimisiz', 2))
# print(find_char_at_index_2('kompyuter', 5))
# print(find_char_at_index('yaxshimisiz', 2))
# print(find_char_at_index('kompyuter', 5))

# Task 3

# def find_char_index(txt1:str, txt2:str):
#     if txt2 in txt1:
#         return txt1.index(txt2)
#     else:
#         return None


# print(find_char_index('yaxshimisiz', 'x'))
# print(find_char_index('salom', 's'))

# Task 4

# def reverse_even_elements(lst:list):
#     length = len(lst)-(len(lst) % 2)
#     for i in range(0,length,2):
#         lst[i],lst[i+1] = lst[i+1],lst[i]
#     return lst

# print(reverse_even_elements([1, 2, 3, 4,5,6,7]))

# Task 5

# def write_matrix(matrix):
#     first, second, third = matrix[0], matrix[1], matrix[2]

#     result = list(first)
#     result.append(second.pop())
#     result.extend(reversed(third))
#     result.extend(list(second))
#     return result

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(write_matrix(matrix))

