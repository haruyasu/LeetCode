from collections import defaultdict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lookup = defaultdict(int)
        candidtates = set()
        for i, c in enumerate(s):
            if lookup[c]:
                candidtates.discard(lookup[c])
            else:
                lookup[c] = i + 1
                candidtates.add(i + 1)
        return min(candidtates) - 1 if candidtates else -1

        
        # Answer some pattern wrong
        # if s == "":
        #     return -1
        # 
        # li2 = []
        # for i in s:
        #     li2.append(i)
        # 
        # if len(set(li2)) == len(s):
        #     return -1
        # 
        # if len(set(li2)) == 1 and len(s) == 2:
        #     return 0
        # 
        # li = []
        # for i in s:
        #     if i in li:
        #         li.remove(i)
        #     else:
        #         li.append(i)
        # 
        # return s.index(li[0])
        

s = "leetcode"
print(Solution().firstUniqChar(s))
# 0

s = "loveleetcode"
print(Solution().firstUniqChar(s))
# 2