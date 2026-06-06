# nums = [3453554,253453435,65456,5535435,153535345]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
# print(nums[0])
        
# nums = [1,2,33,5]
# def total(nums):
#     total = 0
#     for i in range(len(nums)):
#         total = total + nums[i]
#     return total
# print(total(nums))    

# nums = [1,2,2,3]
# freq = {}
# def findOccurrences(nums):
#     for i in range(len(nums)):
#         if nums[i] in freq:
#             return (f"count of {nums[i]} = {freq[nums[i]]}")
#         else:
#             freq[nums[i]] = nums[i]
# print(findOccurrences(nums))            
                    
# nums = [3,1,2]
# nums = [1,2,3]
# def check_sorted(nums):
#     for i in range(len(nums)):
#         if nums[i] > nums[i + 1]:
#             return False
#         else:
#             return True
# print(check_sorted(nums))        

# nums = [1,2,3,3,4,5,5,8,9,3,2,4,6,77,33,55,77]
# final_nums = []
# def remove_dup():
#     for i in range(len(nums)):
#         if nums[i] in final_nums:
#             final_nums.remove(nums[i])
#             final_nums.append(nums[i])
#         else:
#             final_nums.append(nums[i])
#     return final_nums        
# print(remove_dup())           

# nums = [3,2,1,4,0,-1,-2,777]
# min_val = nums[0]
# for i in nums:
#     if i < min_val:
#         min_val = i
# print(min_val)        

# nums = [3,2,4,1, -1]
# min_nums = nums[0]
# for i in nums:
#    if min_nums > i:
#         min_nums = i
# print(min_nums)

nums = [3,4,5,6,7]
def check_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True    
print(check_sorted(nums))