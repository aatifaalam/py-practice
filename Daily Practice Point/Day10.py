nums = [1, 2, 3, 1]
freq = set()
def dup(nums):
    for i in nums:
        if i in freq:
            return True
        else:
            freq.add(1)
    return False        
print(dup(nums))