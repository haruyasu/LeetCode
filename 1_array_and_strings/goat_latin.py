class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        def convert(word):
            if word[0] not in "aeiouAEIOU":
                word = word[1:] + word[:1]
                print(word)
            return word + "ma"
        
        return " ".join(convert(word) + "a" * i for i, word in enumerate(S.split(), 1))

S = "I speak Goat Latin"
print(Solution().toGoatLatin(S))
# "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

S = "The quick brown fox jumped over the lazy dog"
print(Solution().toGoatLatin(S))
# "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
