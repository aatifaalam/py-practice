nums = [3,2,3]
def majorityElement(nums):

    '''
    freq = {}
    for i in range(len(nums)):
        freq[nums[i]] = i
    max = -1    
    ans = -1
    for key, value in freq.items():
        if value > max:
            max = value
            ans = key
    return ans
    '''

    freq = {}
    for value in nums:
        if value in freq:
            freq[value] = freq[value] + 1
        else:
            freq[value] = 1

    max = -1    
    ans = -1
    for key, value in freq.items():
        if value > max:
            max = value
            ans = key
    return ans
print(majorityElement(nums))