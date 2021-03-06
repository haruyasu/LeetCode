class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        result += min(prev, curr)
        return result

s = "00110011"
print(Solution().countBinarySubstrings(s))
# 6

s = "10101"
print(Solution().countBinarySubstrings(s))
# 4

