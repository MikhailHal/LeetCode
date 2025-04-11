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
        hashmap = defaultdict(int)
        ans = prefixSum = 0
        hashmap[0] = 1
        for num in nums:
            prefixSum += num
            ans += hashmap[prefixSum-k]
            hashmap[prefixSum] += 1
        print(ans)
        return ans
# @lc code=end

Solution().subarraySum(nums = [1,1,1], k = 2)