from math import inf
from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        """

        maximum = -inf

        maxleft =  -inf
        maxRight = -inf

        leftMax = [0]*len(nums)
        rightMax = [0]*len(nums)

        for i in range(len(nums)):
            maxleft = max(nums[i], maxleft)
            leftMax[i] = maxleft

        for i in range(len(nums)-1, -1, -1):

            maxRight = max(nums[i], maxRight)
            rightMax[i] = maxRight

        j = 1
        while(j<len(nums)-1):
            maximum = max(maximum, (leftMax[j-1]-nums[j])*rightMax[j+1])
            j+=1

        return  0 if maximum<0 else maximum

a = Solution()
nums = [1,10,3,4,19]
ans = a.maximumTripletValue(nums)