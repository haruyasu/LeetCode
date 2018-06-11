class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
        
word = "USA"
print(Solution().detectCapitalUse(word))
# True

word = "FlaG"
print(Solution().detectCapitalUse(word))
# False
