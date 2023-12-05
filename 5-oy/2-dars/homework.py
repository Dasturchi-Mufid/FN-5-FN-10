# Task 1

# def max_interval(lst:list):

#     if len(lst) < 2:
#        return None

#     max_value = 0
#     length = len(lst)-1
#     result = None

#     for i in range(length):
#         if lst[i+1]-lst[i]>max_value:
#             max_value = lst[i+1]-lst[i]
#             result = (lst[i],lst[i+1])

#     return result

# print(max_interval([1,10,7,851,90,1000,1]))

# Task 2

# def min_interval(lst:list):

#     min_value = 10**10
#     length = len(lst) - 1
#     result = None

#     for i in range(length):
#         interval = lst[i+1] - lst[i]
#         if interval < min_value:
#             min_value = interval
#             result = (lst[i],lst[i+1])
#     return result

# print(min_interval([1,2,5,8,41,45,90]))

# Task 3

# from string import digits

# def calc(lst:list):

#     first = ''
#     operator = ''
#     second = ''

#     for i in lst:
#         if i in digits:
#             first += i
#         else:
#             operator = i
#             break
    
#     for i in lst[::-1]:
#         if i in digits:
#             second += i
#         else:
#             second = second[::-1]
#             break
#     return eval(f'{int(first)} {operator} {int(second)}')

# print(calc(['1','45','/','1','2','8']))

# Task 4

# def reverse_str(txt:str):
#     txt_split = txt.split(' ')[::-1]
#     result = ''
#     for i in txt_split:
#         result += f'{i} '
#     return result

# print(reverse_str('Salom senga oq ko`ngil inson'))

# Task 5

def validate_and_sort_emails(emails):
    valid_emails = []

    for email in emails:
        if email.count('@') == 1:
            local_part, domain_part = email.split('@')
            if local_part and domain_part and '.' in domain_part:
                valid_emails.append(email)


    return valid_emails

# Example usage
email_list = ["user@example.com", "invalid-email", "another@domain.com", "no-at-sign.com"]

valid_emails, invalid_emails = validate_and_sort_emails(email_list)

print("Valid Emails:", valid_emails)
print("Invalid Emails:", invalid_emails)
