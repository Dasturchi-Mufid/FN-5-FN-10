# 1) python fileni yonidagi barcha txt fayllarni umumiy so'zlarini sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak) 
# 2) python fileni yonidagi barcha txt fayllarni ichidagi raqamlarni sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak) 
# 3) python fileni yonidagi barcha txt fayllarni ichidagi gaplarni sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak) 
# 4) python fileni yonidagi barcha txt fayllarni ichidan eng uzun gapni qaytarish topish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak) 
# 5) python fileni yonidagi barcha txt fayllarni ichidan shart belilarni tozalash. (file soni qancha bo'lsa shuncha protses yaratilinishi kerak)

# Task 1

from threading import Thread
import os

def all_words():

    global words
    words = list()
    threads = list()
    files = []

    def process_file(file_name):
        global words
        with open(file_name,'r',encoding='utf-8') as f:
            content = f.read().split()
            words += content
    
    os.chdir('5-oy/9-dars/')


    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            files.append(file)
            thread = Thread(target=process_file,args=(file,))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()


    return f'{len(files)} ta {files} filelar ichida {len(words)} ta so`z'

# Task 2

from threading import Thread
import os

def all_digits():

    global digits
    threads = list()
    digits = 0

    def process_file(file_name):
        global digits
        with open(file_name,'r',encoding='utf-8') as f:
            content = f.read()
            digit = sum(txt.isdigit() for txt in content)
            digits += digit
    
    os.chdir('5-oy/9-dars/')


    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            thread = Thread(target=process_file,args=(file,))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()


    return digits

# Task 3

from threading import Thread
import os

def all_sentences():

    global count
    threads = list()
    count = 0

    def process_file(file_name):
        global count
        with open(file_name,'r',encoding='utf-8') as f:
            for i in f.read().split():
                if i.endswith('.') or i.endswith('?') or i.endswith('!'):
                    count += 1
    
    os.chdir('5-oy/9-dars/')

    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            thread = Thread(target=process_file,args=(file,))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()

    return count

# Task 4

def all_sentences():

    global count
    threads = list()
    count = 0

    def process_file(file_name):
        global count
        with open(file_name,'r',encoding='utf-8') as f:
            for i in f.read().split():
                if i.endswith('.') or i.endswith('?') or i.endswith('!'):
                    count += 1
            # content = f.read()
            # digit = sum(txt.isdigit() for txt in content)
            # count += digit
    
    os.chdir('5-oy/9-dars/')


    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            thread = Thread(target=process_file,args=(file,))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()


    return count

# Task 5

from string import punctuation
def clear_punctuation():

    global count
    threads = list()
    count = 0

    def process_file(file_name):
        global count
        with open(file_name,'r',encoding='utf-8') as f:
            text = f.read()
            for punc in punctuation:
                # print(punc)
                text = text.replace(punc,text)
        with open(file_name,'w') as f:
            f.write(text)
    
    os.chdir('5-oy/9-dars/')


    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            thread = Thread(target=process_file,args=(file,))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()