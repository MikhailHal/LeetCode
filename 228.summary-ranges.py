#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        return []
        
# @lc code=end

print(''.join(Solution().summaryRanges(nums = [0,1,3])))
# ["0->1", "3"]

print(''.join(Solution().summaryRanges(nums = [0,1,2,4,5,7])))
# ["0->2","4->5","7"]

print(''.join(Solution().summaryRanges(nums = [0,2,3,4,6,8,9])))
# ["0","2->4","6","8->9"]

print(''.join(Solution().summaryRanges(nums = [])))
# []

print(''.join(Solution().summaryRanges(nums = [1])))
# ["1"]