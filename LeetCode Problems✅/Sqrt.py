class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x==0 or x==1:
            return x

        l =1
        r = x-1

        while l<=r:
            middle = (l+r)//2
            if middle*middle==x:
                return middle
            elif middle*middle>x:
                r=middle-1
            else:
                l = middle+1

        return r



x = 2
a =Solution()
print(a.mySqrt(x))