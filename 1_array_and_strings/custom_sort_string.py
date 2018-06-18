import collections

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counter, s = collections.Counter(T), set(S)
        # print(counter, s)
        result = [c * counter[c] for c in S]
        # print(result)
        # print([c * counter for c, counter in counter.items() if c not in s])
        result.extend([c * counter for c, counter in counter.items() if c not in s])
        return "".join(result)

s = "cba"
t = "abcd"
print(Solution().customSortString(s, t))
# "cbad"
