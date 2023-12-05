# # from decimal import Decimal

# # def checking(x):
# #     count = 0
# #     vovels = 'aeiou'
# #     for i in x:
# #         if i.lower() in vovels:
# #             count += 1
# #     return count

# # # print(checking('assalom'))

# # data = ['salome','Aolimeeeee','Aeesad']

# # data.sort(key=checking)

# # print(data)
# from random import randint

# def max_sale(data):
#     index = data.index(max(data))
#     return index+1

# def min_sale(data):
#     index = data.index(min(data))
#     return index+1

# # month = [i for i in range(1,13)]
# # sale = [randint(10,99)*1000 for i in range(12)]

# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# sale = [69000, 50000, 79000, 26000, 20000, 20000, 73000, 25000, 62000, 48000, 96000, 60000]

# print(month)
# print(sale)

# middle_sale = round(sum(sale)/len(sale),2)
# maxSale = month[max_sale(sale)]
# minSale = month[min_sale(sale)]

# first = f'12 oyda o`rtacha {middle_sale} USD savdo bo`lgan'
# second = f'Maksimal savdo {maxSale} oyda {max(sale)} USD'
# third = f'Minimal savdo {minSale} oyda {min(sale)} USD'
# fourth = ''

# print(first)

# upper_sale = []
# lower_sale = []
# for i in sale:
#     if i > middle_sale:
#         upper_sale.append(i)
#     else:
#         lower_sale.append(i)
# print(upper_sale)
# print(lower_sale)


# upper_sale = []
# lower_sale = []
# for k,v in zip(month,sale):
    
#     if v > middle_sale:
#         upper_sale.append(k)
#     else:
#         lower_sale.append(k)

# print(upper_sale)
# print(lower_sale)

print(False or False)