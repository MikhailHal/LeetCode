#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

from typing import List
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = ans = 0
        curr = 1
        for right in range(len(nums)):
            if curr >= k:
                continue
            ans += right-left+1
            curr *= nums[right]
            while curr >= k:
                ans -= 1
                curr /= nums[left]
                left += 1
        return ans
# @lc code=end
Solution().numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)