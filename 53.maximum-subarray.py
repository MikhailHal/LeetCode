#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = ans = nums[0]
        for i in range(1, len(nums)):
            should_restart = nums[i] > nums[i] + dp[i-1]
            if should_restart:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
            ans = max(ans, dp[i])
        return ans

# @lc code=end

print("exp:3" + " / " + str(Solution().maxSubArray(nums = [1,-2,3])))
print("exp:6" + " / " + str(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])))
print("exp:1" + " / " + str(Solution().maxSubArray(nums = [1])))
print("exp:23" + " / " + str(Solution().maxSubArray(nums = [5,4,-1,7,8])))