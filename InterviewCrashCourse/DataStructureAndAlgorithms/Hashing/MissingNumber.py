from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        numsSet = set(nums)
        n = len(nums)
        for i in range(n+1):
            if not i in numsSet:
                return i
        """
        n = len(nums)
        expectedSum = n * (n+1) // 2
        actualSum = sum(nums)
        return expectedSum - actualSum
