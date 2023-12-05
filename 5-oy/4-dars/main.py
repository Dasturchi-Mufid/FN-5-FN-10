# def f(a):
#     print('f')
#     def g(b):
#         print('g')
#         return 'Salom'
#     return g
# f('a')
# f('a')('b')

b = 10

def a():
    global b
    b = 3
    return b

print(a())
print(b)

