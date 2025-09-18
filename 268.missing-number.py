#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_total = actual_total = 0
        
        for i in range(n+1):
            expected_total += i

        for num in nums:
            actual_total += num

        return expected_total - actual_total
# @lc code=end

print(Solution().missingNumber([3,0,1])) # 2
print(Solution().missingNumber([0,1])) # 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1])) # 8
print(Solution().missingNumber([1])) # 0