class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        
        ss = (s + s)[1 : -1]
        return ss.find(s) != -1

s = "abab"
print(Solution().repeatedSubstringPattern(s))
# True

s = "aba"
print(Solution().repeatedSubstringPattern(s))
# False

s = "abcabcabcabc"
print(Solution().repeatedSubstringPattern(s))
# True
