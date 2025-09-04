#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List
class Solution:
    class Window:
        size = 0
        total = 0

        def incrementWindow(self, newValue):
            self.total += newValue
            self.size += 1

        def decrementWindow(self, newValue):
            self.total -= newValue
            self.size -= 1

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        left = 0
        window = self.Window()
        for right in range(len(nums)):
            window.incrementWindow(nums[right])
            while window.total >= target:
                ans = min(ans, window.size)
                window.decrementWindow(nums[left])
                left += 1
        return ans
# @lc code=end

print(Solution().minSubArrayLen(3, [3,1,2]))