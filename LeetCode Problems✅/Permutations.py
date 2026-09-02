class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        current_array = []
        ans = []

        def recurse(nums):

            if len(current_array)==len(nums):
                ans.append(list(current_array))
                return

            for num in nums:

                if num not in current_array:
                    current_array.append(num)
                    recurse(nums)
                    current_array.pop()

        recurse(nums)

        return ans

a = Solution()
nums = [1,2,3]
ans = a.permute(nums)
