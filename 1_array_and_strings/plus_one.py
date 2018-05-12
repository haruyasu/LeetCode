class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
        
        # Answer 2
        # p = int("".join(map(str, digits))) + 1
        # res = []
        # for i in str(p):
        #     res.append(int(i))
        # 
        # return res


arr = [1,2,3]
print(Solution().plusOne(arr))
# [1, 2, 4]