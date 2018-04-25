class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def triPartition(nums, target):
            i = 0
            j = 0
            n = len(nums) - 1

            while j <= n:
                if nums[j] < target:
                    nums[i] = nums[j]
                    nums[j] = nums[i]
                    i += 1
                    j += 1
                elif nums[j] > target:
                    nums[j] = nums[n]
                    nums[n] = nums[j]
                    n -= 1
                else:
                    j += 1

        triPartition(nums, 1)


A = [2, 0, 2, 1, 1, 0]
Solution().sortColors(A)
print(A)
