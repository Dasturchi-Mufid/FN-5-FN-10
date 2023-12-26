# 1. shunday generator yozingki u ikkita paramterni int typeda qabul qilsin. Ushbu generator qabul qilgan raqamlar orasidagi tub sonlarni qaytarib bersin
# 2. User class yarating unga username, password, email degan xususiyatlari bo`lsin. Unga xoxlaganingizcha method yozing. ushbu classdan yaratilingan obyekt iteratsiya qilinganida obyektning hususiyatlari(username, password, email)ni qaytarsin 
# 3. Foydalanuvchidan 5 marotaba ism, familiya va yoshini qabul qiling. qabul qilgan 3ta ma`lumotni named tuple ko`rinishida listda saqlang. va ularning ichidan eng yoshi kattasini topib bering
# 4. is va == operatorlarni farqi nimadan iborat sss
# 5. iterable hisoblangan data typelarni yozing 

# Task 1

# from collections import namedtuple

# humans = []
# human = namedtuple('Person',field_names=['fname','lname','age'])

# for i in range(1,6):
#     print(f'{i}-inson ma`lumotlarini kiriting!')
#     print()
#     fname = input('Ism kiriting: ').title()
#     lname = input('Familiya kiriting: ').title()
#     while True:
#         age = input('Yosh kiriting: ')
#         try:
#             age = int(age)
#             break
#         except ValueError:
#             print('Yosh to`gri kiritilmadi. Yoshni butun son kiritish kerak:')
#     print()
#     data = human(fname,lname,age)
#     humans.append(data)


# max_age = 0
# max_age_user = ''
# for h in humans:
#     if max_age < h[2]:
#         max_age = h[2]
#         max_age_user = f'{humans}\nRo`yhat ichidan yoshi eng katta inson {h[0]} {h[1]}. U {h[2]} yoshda'
# print(max_age_user)

# # Task 2

# class User:

#     users = []
    
#     def __init__(self,username,password,email):
#         self.username = username
#         self.password = password
#         self.email = email
#         self.index = 0
#         User.users.append(self)
    
#     def __str__(self):
#         return f'Username: {self.username}\nPassword: ***{self.password[::-4]}\nEmail: {self.email}'

#     def __iter__(self):
#         return iter(User.users)
    
#     def __next__(self):
#         if self.index < len(User.users):
#             result = User.users[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration

#     def set_name(self,old_password,new_username):
#         if self.password == old_password:
#             self.username = new_username

#     def set_password(self,old_password,new_password):
#         if self.password == old_password:
#             self.password = new_password

#     def set_email(self,old_password,new_email):
#         if self.password == old_password:
#             self.username = new_email

    
# user1 = User('a1','b1asdadasdasd','c1')
# user2 = User('a2','b2jghjghjghj','c2')
# user3 = User('a3','b3rtyertyerty','c3')
# user4 = User('a4','b4sdsdfddfgdfg','c4')

# data = iter(user1)
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))

# for i in user1:
#     print(i)


# Task 3


# def prime_nums(number1:int,number2:int):
#     while number1 < number2:
#         for i in range(2,number1):
#             if number1 % i == 0:
#                 number1 += 1
#                 break
#         else:
#             yield number1
#             number1 += 1

# for i in prime_nums(10,20):
#     print(i)

            


