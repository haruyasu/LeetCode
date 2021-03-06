class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        result = []
        row, col, d = 0, 0, 0
        dirs = [(-1, 1), (1, -1)]
        
        for i in range(len(matrix) * len(matrix[0])):
            result.append(matrix[row][col])
            row += dirs[d][0]
            col += dirs[d][1]
            
            if row >= len(matrix):
                row = len(matrix) - 1
                col += 2
                d = 1 - d
            elif col >= len(matrix[0]):
                col = len(matrix[0]) - 1
                row += 2
                d = 1 - d
            elif row < 0:
                row = 0
                d = 1 - d
            elif col < 0:
                col = 0
                d = 1 - d
        return result

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(Solution().findDiagonalOrder(matrix))
# [1,2,4,7,5,3,6,8,9]