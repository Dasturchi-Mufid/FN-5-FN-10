
"""Question before lesson"""

# class Smth:

#     def __len__(self):
#         return True

# a = Smth()
# print(Smth.__len__(a))

""" Мултипоточность """

# First

# from threading import Thread
# from time import sleep, time

# def func_1():
#     print('Birinchi funksiya ishladi.')
#     sleep(3)
#     print('Birinchi funksiya tugadi')

# def func_2():
#     print('Ikkinchi funksiya ishladi.')
#     sleep(3)
#     print('Ikkinchi funksiya tugadi')
    

# th1 = Thread(target=func_1)
# th2 = Thread(target=func_2)

# start = time()

# th1.start()
# th2.start()

# finish = time()
# print(finish-start)

# Second

# from threading import Thread
# from time import sleep,time

# def func_1():
#     print('Birinchi funksiya ishladi.')
#     sleep(3)
#     print('Birinchi funksiya tugadi')

# def func_2():
#     print('Ikkinchi funksiya ishladi.')
#     sleep(3)
#     print('Ikkinchi funksiya tugadi')
    

# th1 = Thread(target=func_1)
# th2 = Thread(target=func_2)

# start = time()

# th1.start()
# th2.start()

# th1.join()
# th2.join()

# finish = time()
# print(finish - start)

# Task 1 --Fail--

# from threading import Thread

# with open('avto.txt') as file:
#     text = file.read().split()
    # print(text)

# names = ['avto','hafta','name','shahar']

# def avto_count():
#     with open('avto.txt') as file:
#         txt_list = file.read().split()
#         print(len(txt_list))

# def shahar_count():
#     with open('shahar.txt') as file:
#         txt_list = file.read().split()
#         print(len(txt_list))

# def hafta_count():
#     with open('hafta.txt') as file:
#         txt_list = file.read().split()
#         print(len(txt_list))

# def name_count():
#     with open('name.txt') as file:
#         txt_list = file.read().split()
#         print(len(txt_list))
    

# th1 = Thread(target=avto_count)
# th2 = Thread(target=name_count)
# th3 = Thread(target=hafta_count)
# th4 = Thread(target=shahar_count)

# th1.start()
# th2.start()
# th3.start()
# th4.start()


