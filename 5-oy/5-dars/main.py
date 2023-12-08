# from models import Week

# print(Week.get_item(1,5,3,5))

# Task 1

# def find_elements(nums:list[int]):
#     max_element = max(nums)
#     min_element = min(nums)
#     result = []
#     for i in range(min_element+1,max_element):
#         if i not in nums:
#             result.append(i)

#     return result

# print(find_elements([20,5,10]))


def find_elements(nums:list[int]):
    max_element = max(nums)
    min_element = min(nums)

    nums.pop(nums.index(max_element))
    nums.pop(nums.index(min_element))

    result1 = set(range(min_element,max_element))
    result2 = set(nums)

    return result1,result2

print(find_elements([2,3,8,20]))