# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            old = result[0] = 1
            for j in range(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result

rowIndex = 3
print(Solution().getRow(rowIndex))
# Output: [1,3,3,1]
