
"""Iterable & iterators"""

# iter() funksiyasi iteratsiya hosil qilib beradi. next() funksiyasi iteratsiyaga tushugan elementni bita bita chaqirib beradi
# iter va next funksiyalari for siklida foydalaniladi. iter,next,StopIteration shu 3 lasiga asoslangan holda ishlaydi for sikli.

numbers = [16,30,7,12,'salom']

iterable = iter(numbers)

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

# for_func(color)


class MyIter:

    def __init__(self,*args):
        self.elements = args
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.elements)>self.index:
            result = self.elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class Myrange:

    def __init__(self,*args):
        
        num_args = len(args)

        # match len(args):
        #     case 0:
        #         raise TypeError("MyRange expected at least 1 argument, got 0")
        #     case 1:
        #         self.start, self.stop, self.step = 0, args[0], 1
        #     case 2:
        #         self.start, self.stop, self.step = args[0], args[1], 1
        #     case 3:
        #         self.start, self.stop, self.step = args
        #     case _:
        #         raise TypeError(f"MyRangega ko`pi bilan 3 ta property berish kerak. Siz {num_args} ta property berdingiz")

        if num_args == 0:
            raise TypeError("MyRangega kamida 1 ta property berish kerak. Siz umuman property bermadingiz")
        elif num_args == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif num_args == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif num_args == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(f"MyRangega ko`pi bilan 3 ta property berish kerak. Siz {num_args} ta property berdingiz")
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.stop > self.start:
            result = self.strat
            self.strat += self.step
            return result
        else:
            raise StopIteration

a = MyIter(1,250,15)
for i in a:
    print(i)
# for i in Myrange(10):
#     print(i)
        




