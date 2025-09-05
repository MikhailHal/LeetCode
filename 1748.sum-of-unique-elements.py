#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
from typing import List
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        map = {}
        ans = 0
        for num in nums:
            if not num in map:
                map[num] = 1
            else:
                map[num] += 1
        
        for key in map:
            if map[key] < 2:
                ans += map[key] * int(key)
        return ans
# @lc code=end

print(Solution().sumOfUnique([1,2,3,2]))
print(Solution().sumOfUnique([1,1,1,1]))
print(Solution().sumOfUnique([1,2,3,4,5]))
print(Solution().sumOfUnique([1]))