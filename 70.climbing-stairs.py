#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# @lc code=end

print(Solution().climbStairs(1)) # 1
print(Solution().climbStairs(2)) # 2
print(Solution().climbStairs(3)) # 3
print(Solution().climbStairs(4)) # 2