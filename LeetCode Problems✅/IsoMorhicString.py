class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dicti = {}
        dicti_2 = {}

        ln = len(s)

        for i in range(ln):
            if s[i] not in dicti and t[i] not in dicti_2:    
                dicti[s[i]]=t[i]
                dicti_2[t[i]]=s[i]
            elif t[i] in dicti and dicti[t[i]]!=s[i]:
                return False
            elif s[i] in dicti_2 and dicti_2[s[i]]!=t[i]:
                return False
            elif s[i] in dicti and dicti[s[i]]!=t[i]:
                return False
            elif t[i] in dicti_2 and dicti_2[t[i]]!=s[i]:
                return False

        return True

a = Solution()
ans = a.isIsomorphic("bar", "foo")
print(ans)
