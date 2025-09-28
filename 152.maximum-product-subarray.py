#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            candidates = [
                max_product * nums[i],
                min_product * nums[i],
                nums[i]
            ]
            max_product = max(candidates)
            min_product = min(candidates)
            ans = max(ans, max_product)
        return ans

# @lc code=end

print("exp:6" + " / " + str(Solution().maxProduct(nums = [2,3,-2,4])))
print("exp:0" + " / " + str(Solution().maxProduct(nums = [-2,0,-1])))
print("exp:1" + " / " + str(Solution().maxProduct(nums = [1])))
print("exp:3" + " / " + str(Solution().maxProduct(nums = [-3,-1,-1])))