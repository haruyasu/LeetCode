import collections

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = collections.defaultdict(list)
        result = []

        for i in strs:
            sorted_str = "".join(sorted(i))
            anagrams_map[sorted_str].append(i)

        for i in anagrams_map.values():
            i.sort()
            result.append(i)

        return result

li = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(li))
