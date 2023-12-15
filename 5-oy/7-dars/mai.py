""" Generators """

# from collections.abc import Iterable# iteratormi yoki yo`qmi tekshirish classi

# print(isinstance('salom',Iterable))

# a = [i for i in range(10)]
# b = (i for i in range(10))

# print(a)
# print(b)

# def a():
#     print('Funksiya ishladi')
#     return True

# def b():
#     print('Generator ishladi')
#     yield True

# a()
# next(b())

# def a():
#     print('Funksiya ishladi')
#     return True

# def b():
#     print('Generator ishladi')
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# a()
# print(next(b()))
# print(next(b()))
# print(next(b()))
# print(next(b()))
# print(next(b()))
# print(next(b())) buni necha marta ishlatsak ham generator ishladi \n1 yozuvi chiqadi. 
# Bunda 1 2 3 qilib chiqarish uchun quyidagi kodni ishlatish kerak.

# c = b()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# from abc import ABC,abstractclassmethod

# class a(ABC):
#     @abstractclassmethod
#     def c(self):
#         pass

# b = a()
# print(b)

# def num():
#     while True:
#         print(1630)
#         yield 1
#         yield 2

# obj = num()

# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

# def num():
#     print('Generator ishladi')
#     yield 1
#     print('Generator ishladi 2')
#     yield 2

# obj = num()

# print(next(obj))
# print(next(obj))
# print(next(obj))

# import string
# import random

# def make_session():
#     return "".join(random.sample(string.ascii_letters+string.digits,20))

# result_1 = [make_session() for _ in range(10)]
# result_2 = (make_session() for i in  range(10))

# def m_s():
#     for _ in range(10):
#         print(_)
#         yield make_session()

# result_3 = m_s()

# print(next(result_3))
# print(next(result_3))
# print(next(result_3))
# print(next(result_3))
# print(next(result_3))
