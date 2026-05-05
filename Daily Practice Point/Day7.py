# dict ={
#     "Aatif": 90,
#     "B": 60,
#     "C": 55,
#     "D": 44,
#     "E": 33,
#     "F": 22,
#     "G": 66
# }
# for key in dict:
#     print(key, dict["E"])
# print(dict["G"])

# names = {
#     'name': "Aatif",
#     'subjects': {
#         'Math': 99,
#         'Physics': 98,
#         'Chemestry': 97
#         },
#     'surname': "Aalam"
# }
# print(f"{names['name']} is passed {names['subjects'].key(0)} with {names['subjects']['Math']} marks.")

# nums = [1, 2, 3, 3 , 2, 4, 4]
# freq_nums ={1: 1, 2: 2, 3: 3, 4: 84}
# for i in nums:
#     if i in freq_nums:
#         freq_nums[i] = freq_nums[i] + 1
#     else:
#         freq_nums[i] = 1
# print(freq_nums)        

# nums = [1, 2, 2, 3, 3, 3]
# freq = {}
# for n in nums:
#     if n in freq:
#         freq[n] = freq[n] + 1
#     else:
#         freq[n] = 1
# print(freq)

# fruit = "bananaf"
# freq = {}
# for n in fruit:
#     if n in freq:
#         freq[n] = freq[n] + 1
#     else:
#         freq[n] = 1
# print(freq)        

# nums = [1, 2, 3]
# freq = {}
# def find_d():
#     for n in nums:
#         if n in freq:
#             return True
#         else:
#             freq[n] = False
#     return False        
# print(find_d())        

# def containsNearbyDuplicate():
#     nums = []
#     for i in range(6):
#         n = int(input("Enter numbers: "))
#         nums.append(n)

#     freq = {}
#     for i in nums:
#         if i in freq:
#             freq[i] = freq[i] + 1
#         else:
#             freq[i] = 1
#     print(freq)        
# ans = containsNearbyDuplicate()
# print(ans)

# nums = []
# for i in range(6):
#     n = int(input("Enter numbers: "))
#     nums.append(n)

# freq = {}
# for i in nums:
#     if i in freq:
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1
# print(freq)    

# nums = []
# for i in range(6):
#     n = int(input("Enter number: "))
#     nums.append(n)
# freq = {}
# for n in nums:
#     if n in freq:
#         freq[n] += 1
#     else:
#         freq[n] = 1
# count = 0  
# ans = 0      
# for x in freq:
#     if freq[x] > count:
#         count = freq[x]
#         ans = x
# print(ans)        
# print(count)        
# print(freq)        

# nums = []
# for i in range(4):
#     n = int(input("Enter number: "))
#     nums.append(n)
# odd = []
# even = []
# for n in nums:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
# ans = {'even': even, 'odd': odd}   
# print(ans)

# def odd_even():
#     nums = []
#     for i in range(6):
#         n = int(input("Enter number: "))
#         nums.append(n)
#     even = []
#     odd = []    
#     for n in nums:
#         if n % 2 == 0:
#             even.append(n)
#         else:
#             odd.append(n)
#     ans = {'even': even, 'odd': odd}
#     return ans
# print(odd_even())
    
# dict = {'a': 1, 'b': 2}
# new_dict = {}
# for d in dict:
#     v = dict[d]
#     new_dict[v] = d
# print(new_dict)

# char = input("Enter characters: ")
# character = "aabbcdde"
# dict = {}
# new_dict = {}
# for i in character:
#     if dict.get(i):
#         dict[i] = dict[i] + 1
#     else:
#         dict[i] = 1        
# for n in dict:
#     if dict[n] == 1:
#         print(n)
#         break

# data = {1:'A', 2:'B', 3:'C'}
# print(data.get(1))    

# keys = ['a', 'b', 'c']
# rooms = [1,2,3,4]
# result = {}
# length = min(len(keys),len(rooms))
# for i in range(length):
#     result[keys[i]] = rooms[i]
# print(result)

# num =[]
# for i in range(3):
#    n = int(input("Enter number: "))
#    num.append(n)

# nums = []
# for i in range(3):
#     n = int(input("Enter number: "))
#     nums.append(n)
# nums.remove(nums[0])    
# print(nums)

# tasks = []
# for i in range(2):
#     t = input("Enter tasks: ")
#     tasks.append(t)
# print(tasks)

# tasks = ["study", "code", "sleep"]
# print(tasks[3])

# data = {'Aatif': 99}
# data['Aatif'] = 98
# print(data['Aatif'])


# def two_sum():
#     nums = [2,11,7,15]
#     target = 9
#     n = 0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j] == target:
#                 return [i, j]
#     return [-1, -1]        
# print(two_sum())          

# def palindrome():
#     x = 10
#     temp = x
#     n = 0
#     while temp > 0:
#         r = temp % 10
#         n = n * 10 + r
#         temp = temp // 10
#     return x == n
# print(palindrome())

def duplicate():
    nums = [1,2,3,1]
    freq = {}
    for i in nums:
        if i in freq:
            return True
        else:
            freq[i] = 1
    return False
print(duplicate())