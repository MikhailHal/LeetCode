#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = ans = nums[0]
        for i in range(1, len(nums)):
            should_restart = nums[i] > nums[i] + current_sum
            if should_restart:
                current_sum = nums[i]
            else:
                current_sum = nums[i] + current_sum
            ans = max(ans, current_sum)
        return ans

# @lc code=end

print("exp:3" + " / " + str(Solution().maxSubArray(nums = [1,-2,3])))
print("exp:6" + " / " + str(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])))
print("exp:1" + " / " + str(Solution().maxSubArray(nums = [1])))
print("exp:23" + " / " + str(Solution().maxSubArray(nums = [5,4,-1,7,8])))