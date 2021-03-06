class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        result = [str(nums[0]) + "/(" + str(nums[1])]
        for i in range(2, len(nums)):
            result += "/" + str(nums[i])
        result += ")"
        return "".join(result)

nums = [1000,100,10,2]
print(Solution().optimalDivision(nums))
# "1000/(100/10/2)"
