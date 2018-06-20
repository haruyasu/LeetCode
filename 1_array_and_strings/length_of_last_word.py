class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])

s = " Hello World"
print(Solution().lengthOfLastWord(s))
# 5