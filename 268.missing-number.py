#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect_xor = actual_xor = 0
        for i in range(len(nums)+1):
            expect_xor ^= i
        
        for num in nums:
            actual_xor ^= num
        
        return expect_xor ^ actual_xor
# @lc code=end

print(Solution().missingNumber([3,0,1])) # 2
print(Solution().missingNumber([0,1])) # 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1])) # 8
print(Solution().missingNumber([1])) # 0