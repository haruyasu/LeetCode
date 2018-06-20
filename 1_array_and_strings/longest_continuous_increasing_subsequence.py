class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] < nums[i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result

nums = [1,3,5,4,7]
print(Solution().findLengthOfLCIS(nums))
# 3

nums = [2,2,2,2,2]
print(Solution().findLengthOfLCIS(nums))
# 1
