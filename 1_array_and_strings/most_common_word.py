import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lookup = set(banned)
        counts = collections.Counter(word.strip("!?',;.") for word in paragraph.lower().split())
        result = ""
        for word in counts:
            if (not result or counts[word] > counts[result]) and word not in lookup:
                result = word
        return result

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
# "ball"
