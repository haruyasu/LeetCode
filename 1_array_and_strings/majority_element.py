class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1
        for i in range(len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1
        return nums[idx]

nums = [3,2,3]
print(Solution().majorityElement(nums))
# 3

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
# 2
