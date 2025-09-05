#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = {}
        ans = 0
        maxFrequency = 0
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        for key in map:
            if map[key] > maxFrequency:
                ans = map[key]
                maxFrequency = map[key]
            elif map[key] == maxFrequency:
                ans += map[key]
        return ans
        
# @lc code=end

print(Solution().maxFrequencyElements([1,2,2,3,1,4]))
print(Solution().maxFrequencyElements([1,2,3,4,5]))
print(Solution().maxFrequencyElements([1,1]))