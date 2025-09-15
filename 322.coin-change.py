#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        
# @lc code=end

print("expected ans:3, " + str(Solution().coinChange([1,2,5], 11)))
print("expected ans:-1, " + str(Solution().coinChange([2], 3)))
print("expected ans:0, " + str(Solution().coinChange([1], 0)))
print("expected ans:2, " + str(Solution().coinChange([1,2,4], 6)))