import collections

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        left, right = {}, {}
        for i, num in enumerate(nums):
            left.setdefault(num, i)
            right[num] = i
        degree = max(counts.values())
        return min(right[num] - left[num] + 1 for num in counts.keys() if counts[num] == degree)

nums = [1, 2, 2, 3, 1]
print(Solution().findShortestSubArray(nums))
# 2

nums = [1,2,2,3,1,4,2]
print(Solution().findShortestSubArray(nums))
# 6
