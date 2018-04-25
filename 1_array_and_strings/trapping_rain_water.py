class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        top = 0
        for i in range(len(height)):
            if height[top] < height[i]:
                top = i

        second_top = 0
        for i in range(top):
            if height[second_top] < height[i]:
                second_top = i
            result += height[second_top] - height[i]

        second_top = len(height) - 1
        for i in reversed(range(top, len(height))):
            if height[second_top] < height[i]:
                second_top = i
            result += height[second_top] - height[i]

        return result


li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(li))
