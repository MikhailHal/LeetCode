#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
"""
1. substructure
・numbers[right] + numbers[left]について
    ・==targetの場合はペアを返却
    ・>targetの場合はright--
    ・<targetの場合はleft++

2. state
・left
・right
・total


3. reccurence relation
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                break
            elif total > target:
                right -= 1
            elif total < target:
                left += 1
        return (left+1, right+1)

# @lc code=end

Solution().twoSum(numbers = [5,25,75], target = 100)
# [2,3]

Solution().twoSum(numbers = [2,3,4], target = 6)
# [1,3]

Solution().twoSum(numbers = [2,7,11,15], target = 9)
# [1,2]

Solution().twoSum(numbers = [-1,0], target = -1)
# [1,2]