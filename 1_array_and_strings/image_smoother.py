class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def getGray(M, i, j):
            total, count = 0, 0.0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    ii, jj = i + r, j + c
                    if 0 <= ii < len(M) and 0 <= jj < len(M[0]):
                        total += M[ii][jj]
                        count += 1.0
            return int(total / count)

        result = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                result[i][j] = getGray(M, i, j)
        return result

M = [[1,1,1], [1,0,1], [1,1,1]]
print(Solution().imageSmoother(M))
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
