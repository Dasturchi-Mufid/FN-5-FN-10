# 1) txt fayldagi so'zlarni sonini qaytaruvchi dastur tuzing 
# 2) txt ichidagi tel raqamlarni validatsiyadan o'tkazadigan dastur yozing 
# 3) txt fayl ichidagi eng oxirgi qatordagi elementlarni qaytaruvchi dastur tuzing 
# 4) raqamlardan iborat list bor, uni ichidagi raqamlar kichikdan kattaga qaratib 
# tartiblanganda buzilgan birin-ketinlikni topuvchi dastur tuzing 
# 5) git va githubni guruhga tashlangan manbalar bo'yicha yaxshilab o'rganib keling

# Task 1

# with open('homework.txt') as f:
#     count = f.read().split()
#     print(len(count))

# Task 2

# with open('phones.txt') as f:
#     phones = f.read().split()
#     valid_phones = []
#     for phone in phones:
#         if len(phone) == 13 and phone.startswith('+') and phone[1::].isdigit():
#             print(f'{phone} validatsiyadan o`tdi')
#             valid_phones.append(phone)
#     print(valid_phones)

# Task 3

# with open('homework.txt') as f:
#     lines = f.read().split('\n')
#     print(lines[-1])

# Task 4

# numbers = [1,2,3,5,4,6,7,8,9]

# if numbers == numbers[::].sort():
#     print(f'{numbers} tartiblangan')
# else:
#     for i in range(len(numbers)):
#         if numbers[i] < numbers[i+1]:
#             continue
#         else:
#             print((numbers[i-1],numbers[i],numbers[i+1]))
#             break
