class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        
        
        # some pattern wrong
        # li = []
        # for i in range(k, 0, -1):
        #     li.append(nums[-i])
        # 
        # for i in range(len(nums) - k):
        #     li.append(nums[i])
        # 
        # for i in range(len(nums)):
        #     nums[i] = li[i]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(arr, k)
print(arr)
# [5, 6, 7, 1, 2, 3, 4]

arr = [-1, -100, 3, 99]
k = 2
Solution().rotate(arr, k)
print(arr)
# [3, 99, -1, -100]