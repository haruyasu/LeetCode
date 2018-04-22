class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = []
        for i in s:
            li.append(i)
        
        li2 = []
        for i in range(len(li) - 1, -1, -1):
            li2.append(li[i])
        
        return "".join(li2)