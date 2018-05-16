class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == (total - left_sum - num):
                return i
            left_sum += num
        return -1
    

nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))
# 3

nums = [1, 2, 3]
print(Solution().pivotIndex(nums))
# -1
