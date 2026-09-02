class Solution:
    def reverse(self, x: int) -> int:
        
        nums = str(x)
        print(nums*2)

        negative = True if "-" in nums else False
        if negative:
            nums = nums[1:]
        placeholder = 10**(len(nums)-1)

        maximum = 2**31 - 1

        i = len(nums)-1
        
        cur_number = 0
        while i>=0:
            if cur_number + int(nums[i])*placeholder <=maximum:
                cur_number =  cur_number + int(nums[i])*placeholder
            else:
                return 0
            i-=1
            placeholder//=10

        return -cur_number*2 if negative else cur_number

a = Solution()
x = -123
ans = a.reverse(x)
print(ans)