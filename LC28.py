arr = [1,1,2,3,3,4,4,5,5]

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        

        k = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
s = Solution()
print(s.removeDuplicates(arr))