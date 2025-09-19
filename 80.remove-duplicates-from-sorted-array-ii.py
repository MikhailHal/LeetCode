#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for read in range(len(nums)):
            if write < 2 or nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write
        
# @lc code=end

Solution().removeDuplicates(nums = [1,1,1,2,2,3])
# 5, nums = [1,1,2,2,3,_]

Solution().removeDuplicates(nums = [0,0,1,1,1,1,2,3,3])
# 7, nums = [0,0,1,1,2,3,3,_,_]

Solution().removeDuplicates(nums = [1])
# 5, nums = [1]