# class yozing u o'zida majburiy bo'lgan append degan methodi bo'lsin. 
# 1) classdan obyekt olib with operatori bilan qo'llash davomida xatolik amalga oshsa barcha append yordamida qo'shilgan elementlar asl holatiga qaytib qolishi kerak. 
# aks xolda xatolik ro'y bermasa natijani saqlab qolsin. (__enter__, __exit__ foydalanish mumkin) 
# 2) class obyekti va with operatori o'rtasini ta'minlab turuvchi conextmeneger funksiya yarating, 
# u with operaotri bilan ishlash davomida xatolik amalga oshsa barcha append yordamida qo'shilgan elementlar asl holatiga qaytib qolishi kerak. 
# aks xolda xatlik ro'y bermasa natijani saqlab qolsin. (__enter__, __exit__ foydalanish mumkin emas)

# Task 1

class Smth:

    cls_elements = []

    def __init__(self):
        self.elements = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with message: {exc_value}")
            self.elements.clear()
            Smth.cls_elements = [i for i in self.elements]
            print(Smth.cls_elements)
        else:
            print("Exiting the context successfully")
            Smth.cls_elements = [i for i in self.elements]
            print(Smth.cls_elements)
    
    def append(self,data):
        self.elements.append(data)

with Smth() as obj:
    obj.append('a')
    obj.append(5)
    raise ValueError


# Task 2

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    elements = []
    correct_elements = []
    print("Konteksga kirish")
    try:
        yield elements
    except Exception as e:
        print(f"Xatolik: {e}")
        elements.clear()
    finally:
        correct_elements = elements
        print(correct_elements)

with my_context_manager() as value:
    value.append(5)
    value.append('s')
    raise ValueError("Xatolik")