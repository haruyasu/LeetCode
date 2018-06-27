class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return palindrome(s, left, right - 1) or palindrome(s, left + 1, right)
            left, right = left + 1, right - 1
        return True

s = "aba"
print(Solution().validPalindrome(s))
# True

s = "abca"
print(Solution().validPalindrome(s))
# True
