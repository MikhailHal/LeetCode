#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appears = set()
        for num in nums:
            if num in appears:
                return True
            appears.add(num)
        return False
        
# @lc code=end

print(Solution().containsDuplicate([1,2,3,4]))