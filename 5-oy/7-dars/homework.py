# 1) password yaratib bberuvchi generator yarating 
# 2) generator bitta raqamni qabul qilsin va shu raqamgacha bo`lgan juft sonlari qaytaruvchi generator yozing 
# 3) generator bitta raqamni qabul qilsin va shu raqamgacha bo`lgan toq sonlari qaytaruvchi generator yozing 
# 4) generator bitta raqamni qabul qilsin va shu raqamgacha bo`lgan tub sonlarni qayarsin

# Task 1

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + '.,@!-_()'
    # password = ''.join(random.choice(characters) for i in range(length))
    password = ''.join(random.sample(characters,length)) # second way
    return password

# Task 2

def generate_even_numbers(n):
    for i in range(2,n+1,2):
        yield i

# Task 3

def generate_odd_numbers(n):
    for i in range(1,n+1,2):
        yield i

# Task 4

def generate_prime_numbers_combined(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
