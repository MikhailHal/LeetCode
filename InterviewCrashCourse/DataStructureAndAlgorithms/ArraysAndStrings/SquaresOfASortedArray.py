from typing import List
from math import ceil
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        startIndex = ansIndex = 0
        endIndex = len(nums) - 1
        while startIndex <= endIndex:
            if abs(nums[startIndex]) < abs(nums[endIndex]):
                ans[ansIndex] = nums[endIndex] ** 2
                endIndex -= 1
            else:
                ans[ansIndex] = nums[startIndex] ** 2
                startIndex += 1
            ansIndex += 1
        ans.reverse()
        return ans