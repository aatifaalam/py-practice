from math import inf
class Solution:
    def minimumSum(self, nums) -> int:
        """
        i < j < k
        nums[i] < nums[j] and nums[k] < nums[j]

        at any point 3 index needs to be checked

        """

        j= 1

        ans = +inf

        while j < len(nums):
            i = j-1
            minI = +inf
            while i>=0:
                if nums[i]<nums[j]:
                    minI = min(minI, nums[i])
                i-=1
            k = j + 1
            minK = +inf
            while k<len(nums):
                if nums[k]<nums[j]:
                    minK = min(minK, nums[k])
                k+=1
            if (minI!=inf and minK!=inf):
                ans = min(ans,  nums[j] + minI + minK)
            j+=1

        return ans
        

a = Solution()
nums = [5,4,8,7,10,2]
ans = a.minimumSum(nums)
print(ans)
        