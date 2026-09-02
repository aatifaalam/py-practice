from math import inf
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        dict_map = {}
        for i in range(1, n+1):
            dict_map[i] = False

        for x in nums:
            if x in dict_map:
                dict_map[x] = True

        minimum = inf
        minimum_2 = -inf
        for key, value in dict_map.items():
            if value==False:
                minimum = min(minimum, key)
            else:
                minimum_2 = max(minimum_2, key)
        return minimum if minimum!=inf else minimum_2+1
            
        
a = Solution()
nums = [1,2,3]
ans = a.firstMissingPositive(nums)
print(ans)