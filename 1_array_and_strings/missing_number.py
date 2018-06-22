class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)

        # another solution
        # li = []
        # for i in range(len(nums)):
        #     li.append(i)
        # li.append(sorted(nums)[-1])
        # r = set(li) - set(nums)
        # for i in r:
        #     return i

nums = [3,0,1]
print(Solution().missingNumber(nums))
# 2

nums = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(nums))
# 8
