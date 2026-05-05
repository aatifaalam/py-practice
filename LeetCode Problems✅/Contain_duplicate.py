nums = [3, 3]
freq = set()
def check_duplicate(nums, freq):
    for i in nums:
        if i in freq:
            return True
        else:
            freq.add(i)
    return False
print(check_duplicate(nums, freq))        