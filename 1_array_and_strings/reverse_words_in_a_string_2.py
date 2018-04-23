class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(s, begin, end):
            for i in range(int((end - begin) / 2)):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        reverse(s, 0, len(s))
        print(s)
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1


s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Solution().reverseWords(s)
print(s)
