# from threading import Thread
# import threading

# print(threading.active_count())

# def a():
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(10)

# def b():
#     print(threading.active_count())
#     print(20)

# print(threading.active_count())

# th1 = Thread(target=a)
# th2 = Thread(target=b)

# print(threading.active_count())

# th1.start()
# th2.start()

# print(threading.active_count())

# m1 = th1.join()
# m2 = th2.join()

# print(m1,m2)
# print(threading.__all__)

# import threading

# def my_function(arg1, arg2):
#     # Your function logic here
#     result = arg1 + arg2
#     return result

# def thread_function(arg1, arg2, result_holder):
#     result = my_function(arg1, arg2)
#     result_holder.append(result)

# # Example usage
# if __name__ == "__main__":
#     # Define arguments for your function
#     arg1 = 10
#     arg2 = 20

#     # Create a list to hold the result from the thread
#     result_holder = []

#     # Create a thread and pass your function and its arguments
#     my_thread = threading.Thread(target=thread_function, args=(arg1, arg2, result_holder))

#     # Start the thread
#     my_thread.start()

#     # Wait for the thread to finish
#     my_thread.join()

#     # Access the result from the thread through the result_holder
#     result_from_thread = result_holder[0]
#     print(result_holder)
    
#     print("Result from thread:", result_from_thread)


# from threading import Thread
# import os

# def all_words():

#     global words
#     words = list()
#     threads = list()
#     vowels = 'aeiou'

#     def process_file(file_name):
#         global words
#         with open(file_name,'r',encoding='utf-8') as f:
#             content = f.read().lower()
#             counter = 0
#             for letter in content:
#                 if letter in vowels:
#                     counter += 1
#             words.append({'file name':file_name,'counter':counter})
    
#     os.chdir('5-oy/10-dars/')


#     for file in os.listdir(os.getcwd()):
#         if file.endswith('.txt'):
#             thread = Thread(target=process_file,args=(file,))
#             threads.append(thread)
#             thread.start()
    
#     for thread in threads:
#         thread.join()


#     return words

# print(all_words())

import threading

results = []

def max_word(file_path):

    global results
    
    with open(file_path,'r') as f:
        content = f.read().split()
        content.sort(key=len)
        results.append({'file name':file_path,'max length':content[-1]})
        return f'{file_path} da eng uzun so`z {content[-1]}'

# print(max_word('5-oy/10-dars/ismlar.txt'))

th1 = threading.Thread(target=max_word,args=('5-oy/10-dars/ismlar.txt',))
th2 = threading.Thread(target=max_word,args=('5-oy/10-dars/mashinalar.txt',))
th3 = threading.Thread(target=max_word,args=('5-oy/10-dars/shaharlar.txt',))

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

print(results)