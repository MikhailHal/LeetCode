#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2,len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[len(nums)]

# @lc code=end

print("expected ans:4, " + str(Solution().rob([1,2,3,1])))
print("expected ans:12, " + str(Solution().rob([2,7,9,3,1])))
print("expected ans:1, " + str(Solution().rob([1])))