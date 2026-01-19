#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
"""
部分問題
i段目時点で、その段数にたどり着く方法が何通りあるか。

例外
i=0,1,2は手動初期化

状態
i段目へ上れる通りの数

状態遷移
dp[i] = dp[i-1] + dp[i-2]

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# @lc code=end
print(Solution().climbStairs(1)) #1
print(Solution().climbStairs(2)) #2
print(Solution().climbStairs(3)) #3