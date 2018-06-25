class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or r * c != len(nums) * len(nums[0]):
            return nums
        result = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                result[int(count / c)][count % c] = nums[i][j]
                count += 1
        return result

nums = [[1,2], [3,4]]
r = 1
c = 4
print(Solution().matrixReshape(nums, r, c))
# [[1,2,3,4]]

nums = [[1,2], [3,4]]
r = 2
c = 4
print(Solution().matrixReshape(nums, r, c))
# [[1,2],[3,4]]
