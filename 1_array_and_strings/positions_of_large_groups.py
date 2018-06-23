class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans

S = "abbxxxxzzy"
print(Solution().largeGroupPositions(S))
# [[3,6]]

S = "abc"
print(Solution().largeGroupPositions(S))
# [[]]

S = "abcdddeeeeaabbbcd"
print(Solution().largeGroupPositions(S))
# [[3,5],[6,9],[12,14]]
