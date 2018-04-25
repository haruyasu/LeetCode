class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_seen = []
        
        for i, item in enumerate(nums):
            if (target - item) in number_seen:
                
                for j, item2 in enumerate(number_seen):
                    if target - item == item2:
                        li = []
                        li.append(j)
                        li.append(i)
                return li
            else:
                number_seen.append(item)