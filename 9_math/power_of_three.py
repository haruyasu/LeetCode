import math

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()

n = 9
print(Solution().isPowerOfThree(n))
# True

