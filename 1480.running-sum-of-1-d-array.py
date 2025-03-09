#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

from typing import List

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum: List[int] = list()
        for i, num in enumerate(nums):
            if(i == 0):
                runningSum.append(num)
            else:
                runningSum.append(num + runningSum[i-1])
        return runningSum

        
# @lc code=end
