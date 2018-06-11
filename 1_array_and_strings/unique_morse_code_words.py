class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]
        lookup = {"".join(MORSE[ord(c) - ord("a")] for c in word) for word in words}
        return len(lookup)

words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))
# 2
