class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        length = len(nums)

        for i in range(length):
             comlement = 0 - nums[i]
             twoSumResult = self.twoSum(i+1, nums,comlement )
             ans_result = [nums[x] for x in range(len(twoSumResult))]
             ans_result.append(nums[i])
             if(len(ans_result)==3):
                  ans.append(ans_result)

        return ans

    def twoSum(self, i, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            num_dict = {}
            for j in range(i, len(nums)):
                num = nums[j]
                complement = target - num
                if complement in num_dict:
                    return [num_dict[complement], j]
                num_dict[num] = j
            return []

a = Solution()
nums = [-1,0,1,2,-1,-4]
a.threeSum(nums)