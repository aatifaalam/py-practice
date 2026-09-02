class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []

        for i in range(len(nums)):
            newTarget = target - nums[i]
            ans_1 = self.twoSum(i+1,nums, newTarget)
            for j in ans_1:
                second_level_target = newTarget - nums[j]
                ans_2 = self.twoSum(j+1, nums, second_level_target)
                current_ans = [nums[i], nums[j]]
                for x in ans_2:
                    current_ans.append(nums[x])
                ans.append(current_ans)
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
                return [num_dict[complement], i]
            num_dict[num] = i
        return []


a = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
ans = a.fourSum(nums, target)