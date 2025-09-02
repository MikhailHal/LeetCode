#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(len(nums) - 1):
            if nums[right] == nums[right + 1]:
                nums[right] *= 2
                nums[right + 1] = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
# @lc code=end

print(Solution().applyOperations([1,2,2,1,1,0]))