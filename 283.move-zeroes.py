#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
        print(nums)
        
# @lc code=end

Solution().moveZeroes([0,1,2])
Solution().moveZeroes([1,0,1])
Solution().moveZeroes([1])
Solution().moveZeroes([0,1])
Solution().moveZeroes([0,1,0,3,12])