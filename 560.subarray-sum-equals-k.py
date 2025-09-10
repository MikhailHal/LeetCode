#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return
# @lc code=end

print(Solution().subarraySum(nums = [1,2,3], k = 3)) #2
print(Solution().subarraySum(nums = [1,1,1], k = 2)) #2
print(Solution().subarraySum(nums = [1], k = 0)) #0