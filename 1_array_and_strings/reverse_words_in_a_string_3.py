# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sp = s.split(" ")
        li = []
        for i in sp:
            li.append(i[::-1])
        
        return " ".join(li)

s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
# Output: "s'teL ekat edoCteeL tsetnoc"
