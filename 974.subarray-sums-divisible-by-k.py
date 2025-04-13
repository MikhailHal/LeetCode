#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = ans = 0
        hm = {}
        hm[0] = 1

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k
            if mod in hm:
                ans += hm[mod]
                hm[mod] += 1
            else:
                hm[mod] = 1
        print(ans)
        return ans
        
# @lc code=end
Solution().subarraysDivByK(nums = [1,2,6], k = 2)
"""
(prefix_sum - x) % k = 0
((prefix_sum % k) - (x % k)) % k = 0
prefix_sum % k = x % k
"""