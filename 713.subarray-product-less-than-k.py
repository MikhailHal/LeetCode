#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

from typing import List
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
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
        print(ans)
        """
        if k <= 1:  # Edge case: no subarray can have product < 1
            return 0
            
        left = 0
        ans = 0
        curr = 1
        
        for right in range(len(nums)):
            # Expand window by including the new element
            curr *= nums[right]
            
            # Shrink window from left while product is too large
            while curr >= k and left <= right:
                curr /= nums[left]
                left += 1
            
            # Count valid subarrays ending at 'right'
            # (only after ensuring the window is valid)
            ans += right - left + 1
        
        return ans
        return ans
# @lc code=end
Solution().numSubarrayProductLessThanK(nums = [1,2,3], k = 0)