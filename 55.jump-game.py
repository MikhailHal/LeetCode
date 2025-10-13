#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
"""
1. substructure
・ith時点に到達可能か
・ith+nums[i]はlen(nums)-1(最終段)か
・ith時点での最高到達可能段数は何か

2. state
・ith時点での最も遠い最高到達段数(farthest_step)


3. recurrence relation
・farthest_step = max(farthest_step, i+nums[i])

"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_path = 0
        for i in range(len(nums)):
            # ithに到達不可能
            if farthest_path < i:
                return False
            # ithから最終段まで到達可能
            reachable_step = i + nums[i]
            if reachable_step >= len(nums) - 1:
                return True
            else:
                farthest_path = max(farthest_path, reachable_step)
        return False
# @lc code=end

Solution().canJump(nums = [2,3,1,1,4])
# true

Solution().canJump(nums = [3,2,1,0,4])
# false