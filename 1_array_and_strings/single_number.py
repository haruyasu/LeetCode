import operator
from functools import reduce

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return reduce(operator.xor, nums)
        
        # Answer 2
        # li = []
        # for i in range(len(nums)):
        #     if nums[i] in li:
        #         li.remove(nums[i])
        #     else:
        #         li.append(nums[i])
        # 
        # for i in li:
        #     return i

arr = [2, 2, 1]
print(Solution().singleNumber(arr))
# 1

arr = [4, 1, 2, 1, 2]
print(Solution().singleNumber(arr))
# 4
