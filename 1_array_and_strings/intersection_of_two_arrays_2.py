class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        
        it1 = 0
        it2 = 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res.append(nums1[it1])
                it1 += 1
                it2 += 1
        return res

nums1 = [1, 2, 2, 1, 3, 4, 5]
nums2 = [2, 2, 3, 5, 6]
print(Solution().intersect(nums1, nums2))
# [2, 2, 3, 5]
