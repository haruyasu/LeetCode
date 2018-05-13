class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0
            
                    
        # Answer 2
        # count = 0
        # li = []
        # for i in range(len(nums)):
        #     if 0 == nums[i]:
        #         count += 1
        #     else:
        #         li.append(nums[i])
        # 
        # for i in range(count):
        #     li.append(0)
        # 
        # nums[:] = li[:]

arr = [0, 1, 0, 3, 12]
Solution().moveZeroes(arr)
print(arr)
# [1, 3, 12, 0, 0]
