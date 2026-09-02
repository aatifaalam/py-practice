from math import inf
class Solution:
    def minimumSum(self, nums) -> int:
        """
        i < j < k
        nums[i] < nums[j] and nums[k] < nums[j]

        at any point 3 index needs to be checked

        find leftMinPrefix and find rightMinPrefix

        """

        minimumLeft = inf
        minimumRight = inf

        leftMin = [0]*len(nums)
        rightMin = [0]*len(nums)

        for i in range(len(nums)):
            minimumLeft = min(nums[i], minimumLeft)
            leftMin[i] = minimumLeft

        for i in range(len(nums)-1, -1, -1):

            minimumRight = min(nums[i], minimumRight)
            rightMin[i] = minimumRight
        answerMin = inf
        for j in range(1, len(nums)-1, 1):
            if(nums[j]>leftMin[j-1] and nums[j]>rightMin[j+1]):
                answerMin = min(answerMin, nums[j]+leftMin[j-1]+rightMin[j+1])
        return -1 if answerMin==inf else answerMin

        

a = Solution()
nums = [6,5,4,3,4,5]
ans = a.minimumSum(nums)
print(ans)
        