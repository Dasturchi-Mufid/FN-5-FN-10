# quyidagi masalarni yeching 1) ikkita str element bor. birinchidagi str objdagi barcha element ikkinchi strda borligiga tekshiring 
# 2) lisni ichidagi barcha raqamlarni o`chirib palindromlikga tekshiring 
# 3) qavslar to`g`ri ochilish va yopilish holatini tekshiradigan dastur tuzing. (), {}, [] har hil turdagi qavslar aralash kelishi mumkin 

# Task 1

str1 = "salom"
str2 = "Assalom"

if all(char in str2 for char in str1):
    print("Barcha elementlar topildi.")
else:
    print("Barcha elementlar topilmadi.")

# Task 2

my_list = ['asd','qwe','zxc','qwe','asd']
my_list = list(filter(lambda x: not str(x).isdigit(), my_list))

if my_list == my_list[::-1]:
    print(f"{my_list} list - palindrom")
else:
    print(f"{my_list} list - palindrom emas")

# Task 3

def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= dict[a]:
                    return False
        return stack == []


