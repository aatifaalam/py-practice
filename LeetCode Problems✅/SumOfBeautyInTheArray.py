from typing import List
from math import inf
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:

        leftArray = [[0] * 2 for _ in range(len(nums))]
        rightArray = [[0] * 2 for _ in range(len(nums))]

        minimum = inf
        maximum = -inf

        for i in range(len(nums)):
            minimum = min(nums[i], minimum)
            maximum = max(nums[i], maximum)

            leftArray[i][0] = minimum
            leftArray[i][1] = maximum

        minimum = inf
        maximum = -inf

        for i in range(len(nums)-1, -1, -1):
            minimum = min(nums[i], minimum)
            maximum = max(nums[i], maximum)
            rightArray[i][0] = minimum
            rightArray[i][1] = maximum


        answer = 0

        for i in range(1, len(nums)-1, 1):
            #condition 1
            if nums[i]>leftArray[i-1][1] and nums[i]>leftArray[i-1][0] and nums[i]<rightArray[i+1][0] and nums[i]<rightArray[i+1][1]:
                answer+=2
            elif nums[i]>nums[i-1] and nums[i]<nums[i+1]:
                answer+=1


        return answer


a = Solution()
nums = [2,4,6,4]
a.sumOfBeauties(nums)