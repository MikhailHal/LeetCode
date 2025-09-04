#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        total = 0
        ans = 0
        for num in nums:
            total += num
            if hm.get(total - k):
                ans += hm.get(total - k)
            hm[total] += 1
        return ans
# @lc code=end

Solution().subarraySum(nums = [1], k = 0)