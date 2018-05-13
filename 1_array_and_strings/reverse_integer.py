class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x
        
        # Answer2
        # s = str(x)
        # 
        # if x < 0:
        #     ss = s[1:]
        #     r = ss[::-1]
        #     if int(r) >= 0x7FFFFFFF:
        #         return 0
        # 
        #     return int(r) * -1
        # 
        # else:
        #     r = s[::-1]
        #     if int(r) >= 0x7FFFFFFF:
        #         return 0
        #     return int(r)

x = 123
print(Solution().reverse(x))
# 321

x = -123
print(Solution().reverse(x))
# -321

x = 120
print(Solution().reverse(x))
# 21

