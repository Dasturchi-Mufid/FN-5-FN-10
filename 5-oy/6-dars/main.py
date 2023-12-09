
"""Iterable & iterators"""

# iter() funksiyasi iteratsiya hosil qilib beradi. next() funksiyasi iteratsiyaga tushugan elementni bita bita chaqirib beradi
# iter va next funksiyalari for siklida foydalaniladi. iter,next,StopIteration shu 3 lasiga asoslangan holda ishlaydi for sikli.

# numbers = [16,30,7,12,'salom']

# iterable = iter(numbers)

# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))


def for_func(lst:list):
    iterable = iter(lst)
    while True:
        try:
            print(next(iterable))
        except:
            break

color = ['oq','qora','yashil','sariq']

for_func(color)


