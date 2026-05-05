nums = [2, 15, 11, 7]
target = 18
def two_sum(nums, target):
    freq = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in freq:
            return freq[c], i
        else:
            freq[nums[i]] = i
    return [-1, -1]        
print(two_sum(nums, target))        