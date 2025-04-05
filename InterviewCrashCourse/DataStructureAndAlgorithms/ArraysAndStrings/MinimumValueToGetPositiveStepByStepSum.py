from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = curr = 0
        for i in range(len(nums)):
            curr = nums[i] + curr
            ans = min(ans, curr)
        ans = abs(ans) + 1
        return ans
    
Solution().minStartValue([-3,2,-3,4,2])