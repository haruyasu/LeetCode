class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range(int((len(row) + 1) / 2)):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
            return A


A = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(A))
# [[1,0,0],[0,1,0],[1,1,1]]
