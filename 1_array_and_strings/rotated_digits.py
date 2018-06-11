class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        invalid, diff = set(["3", "4", "7"]), set(["2", "5", "6", "9"])
        result = 0
        for i in range(N + 1):
            lookup = set(list(str(i)))
            if invalid & lookup:
                continue
            if diff & lookup:
                result += 1
        return result

N = 10
print(Solution().rotatedDigits(N))
# 4
