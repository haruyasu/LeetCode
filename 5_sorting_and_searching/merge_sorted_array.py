class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last -= 1
                i -= 1
            else:
                nums1[last] = nums2[j]
                last -= 1
                j -= 1

        while j >= 0:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1


nums1 = [1, 2, 3, 0, 0, 0, 0]
nums2 = [2, 3, 4, 5]
Solution().merge(nums1, 3, nums2, 4)
print(nums1)
