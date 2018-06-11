class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))

a = "aba"
b = "cdc"
print(Solution().findLUSlength(a, b))
# 3
