# 1) Hafta kunlari hisoblaydigan. class yozing. o`sha classning obyekti iteratsiyaga tushganda hafta kunlarining elementlarini qaytarsin 
# 2) Oylar hisoblaydigan class yozing. o`sha classni obyektini iteratsiaya solganda oylar ketma-ketligini qaytarsin 
# 3) User degan class yarating, 3ta xususiyati bo`lsin. 1) f_name 2) l_name, 3) email.
# User obyektini iteratsiyaga solganda shu class asosida yaratilingan obyektlarni qaytarsin.

# Task 1

class Week:
    
    """
    Obyekt yaratilayotganda unga 2 tagacha element berish mumkin.
    Bitta element berilsa, masalan 4 unda 4 ta hafta kuni chiqadi.
    Ikkita element berilsa masalan 2, 6 unda 2-hafta kunidan 6-kungacha chiqadi
    Uch va undan ortiq element berilsa, Type error xatoligi chiqadi 
    """
    
    week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    def __init__(self,*args):
        self.index = 0
        match len(args):
            case 0:
                self.days = Week.week_days
            case 1:
                self.days = Week.week_days[:args[0]]
            case 2:
                self.days = Week.week_days[args[0]:args[1]]
            case _:
                raise TypeError('Week.__doc__ orqali bu classdan qanday qilib ishlash mumkinligi haqida tanishib chiqing.')

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.index <= len(self.days)-1:
                res = self.days[self.index]
                self.index += 1
                return res
            else:
                raise StopIteration


class Month:

    """
    Obyekt yaratilayotganda unga 2 tagacha element berish mumkin.
    Bitta element berilsa, masalan 4, unda 4 ta oy chiqadi.
    Ikkita element berilsa masalan 2, 6 unda 2-oydan 6-oygacha chiqadi
    Uch va undan ortiq element berilsa, Type error xatoligi chiqadi 
    """
    
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']

    def __init__(self,*args):
        self.index = 0
        match len(args):
            case 0:
                self.month = Month.months
            case 1:
                self.month = Month.months[:args[0]]
            case 2:
                self.month = Month.months[args[0]:args[1]]
            case _:
                raise TypeError('Month.__doc__ orqali bu classdan qanday qilib ishlash mumkinligi haqida tanishib chiqing.')


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index <= 11:
            res = self.month[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration

class User:

    users = []
    
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.index = 0
        User.users.append(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(User.users):
            res = User.users[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration
        
    def __str__(self):
        return f'{self.fname} {self.lname}'


