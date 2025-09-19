#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
# @lc code=end

Solution().removeElement(nums = [3,2,2,3], val = 3)
# 2

Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
# 5