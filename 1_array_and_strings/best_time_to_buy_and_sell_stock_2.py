class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

arr = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(arr))
# 7

arr = [1, 2, 3, 4, 5]
# print(Solution().maxProfit(arr))
# 4

arr = [7, 6, 4, 3, 1]
# print(Solution().maxProfit(arr))
# 0