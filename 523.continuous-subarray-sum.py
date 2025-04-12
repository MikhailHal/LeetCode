#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr = 0
        maps = defaultdict(int)
        maps[0] = -1
        for i, num in enumerate(nums):
            curr += num
            if curr%k in maps:
                if i-maps[curr%k] > 1:
                    return True
            else:
                maps[curr%k] = i
        return False
# @lc code=end
print(Solution().checkSubarraySum(nums = [0], k = 1))
"""
(curr-x) % k = 0
((curr%k) - (x%k)) % k = 0
curr%k = x%k
"""