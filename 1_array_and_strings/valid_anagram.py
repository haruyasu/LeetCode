class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        for c in s:
            if c.lower() in count:
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1
        
        for c in t:
            if c.lower() in count:
                count[c.lower()] -= 1
            else:
                count[c.lower()] = -1
            
            if count[c.lower()] < 0:
                return False
        
        return True

        # Answer
        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # else:
        #     return False

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
# True

s = "rat"
t = "cat"
print(Solution().isAnagram(s, t))
# False
