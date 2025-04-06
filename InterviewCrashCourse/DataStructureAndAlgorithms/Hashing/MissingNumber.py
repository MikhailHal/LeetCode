from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        n = len(nums)
        for i in range(n+1):
            if not i in numsSet:
                return i
