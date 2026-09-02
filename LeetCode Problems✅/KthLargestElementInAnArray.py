from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        uniqueSet = set(nums)
        while nums:
            smallest = min(nums)
            nums.remove(smallest)
            uniqueSet.add(smallest)
        return uniqueSet

a = Solution()
nums = [3,2,3,1,2,4,5,5,6]

k = 4
ans = a.findKthLargest(nums, k)
print(ans)