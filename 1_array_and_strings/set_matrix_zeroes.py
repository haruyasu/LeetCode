from functools import reduce

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_col = reduce(lambda acc, i: acc or matrix[i][0] == 0, range(len(matrix)), False)
        first_row = reduce(lambda acc, j: acc or matrix[0][j] == 0, range(len(matrix[0])), False)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        return matrix

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(Solution().setZeroes(matrix))
# [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]