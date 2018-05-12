class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(nums) > len(set(nums))

        # some pattern wrong
        # li = []
        # for i in range(len(nums)):
        #     if nums[i] in li:
        #         return True
        #     else:
        #         li.append(nums[i])
        # 
        # return False

arr = [1,2,3,1]
print(Solution().containsDuplicate(arr))
# True

arr = [1,2,3,4]
print(Solution().containsDuplicate(arr))
# False

arr = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(arr))
# True