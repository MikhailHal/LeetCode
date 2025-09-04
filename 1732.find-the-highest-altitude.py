#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0]
        ans = 0
        for i in range(len(gain)):
            prefixSum.append(prefixSum[i] + gain[i])
            ans = max(ans, prefixSum[i+1])
        return ans
# @lc code=end

print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))