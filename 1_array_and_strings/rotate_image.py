class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        li = []
        for i in zip(*matrix):
            li.append(list(reversed(i)))
        
        return li

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(Solution().rotate(matrix))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]