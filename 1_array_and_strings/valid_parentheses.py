class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = []
        lookup = {"(": ")", "{": "}", "[": "]"}

        for i in s:
            if i in lookup:
                li.append(i)
            elif len(li) == 0 or lookup[li.pop()] != i:
                return False
        return len(li) == 0


print(Solution().isValid("()[]{}"))
print(Solution().isValid("([]{"))
