# Given a binary array, find the maximum number of consecutive 1s in this array.
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        local_max = 0
        for i in nums:
            if i == 1:
                local_max += 1
            else:
                local_max = 0
            result = max(result, local_max)
        return result

nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
