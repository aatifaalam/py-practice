class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        current_array = []
        ans = []
        
        def recurse(nums):

            if len(current_array)==len(nums):
                ans.append([nums[x] for x in current_array])
                return

            for i in range(len(nums)):
                if i not in current_array:
                    if i==0 or (i > 0 and nums[i]==nums[i-1])==False or (i>0 and nums[i-1]==nums[i] and i-1 in current_array):
                        current_array.append(i)
                        recurse(nums)
                        current_array.pop()

        nums.sort()
        recurse(nums)

        return ans

a = Solution()
nums = [1,1,2]
ans = a.permuteUnique(nums)