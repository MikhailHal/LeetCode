#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        dp[0] = 0
        buy = 0
        for i in range(1, len(prices)):
            # 最安値の場合を常に更新
            if prices[buy] > prices[i]:
                buy = i
            # 現時点で売却した場合を最高利益を計算
            profit = prices[i] - prices[buy]
            if profit > 0:
                dp[i] = max(dp[i-1], profit)
            else:
                dp[i] = dp[i-1]
        return dp[len(prices) - 1]

# @lc code=end

Solution().maxProfit(prices = [7,1,5,3,6,4])
# 5

Solution().maxProfit(prices = [2,4,1])
# 2


Solution().maxProfit(prices = [7,6,4,3,1])
# 0

Solution().maxProfit(prices = [1])
# 0