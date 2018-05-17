class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1

nums = [3, 6, 1, 0]
print(Solution().dominantIndex(nums))
# 1

nums = [1, 2, 3, 4]
print(Solution().dominantIndex(nums))
# -1
