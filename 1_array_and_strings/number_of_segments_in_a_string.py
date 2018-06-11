class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.strip().split(" ") if i])

s = "Hello, my name is John"
print(Solution().countSegments(s))
# 5