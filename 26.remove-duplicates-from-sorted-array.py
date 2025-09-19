#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)
# @lc code=end

Solution().removeDuplicates(nums = [1,1,2])
# 2, [1,2,_]

Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])
# 5, [0,1,2,3,4,_,_,_,_,_]

Solution().removeDuplicates(nums = [1])
# 1, [1]