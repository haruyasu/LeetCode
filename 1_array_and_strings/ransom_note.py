import collections

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = collections.Counter(ransomNote)
        b = collections.Counter(magazine)
        return not a - b

a = "a"
b = "b"
print(Solution().canConstruct(a, b))
# false

a = "aa"
b = "ab"
print(Solution().canConstruct(a, b))
# false

a = "aa"
b = "aab"
print(Solution().canConstruct(a, b))
# true
