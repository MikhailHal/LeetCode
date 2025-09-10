#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict = {0: 1}
        ans = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            
            target_key = sum - k
            if target_key in dict:
                ans += dict[target_key]
            if sum in dict:
                dict[sum] += 1
            else:
                dict[sum] = 1
        return ans
# @lc code=end

print(Solution().subarraySum(nums = [1,2,3], k = 3)) #2
print(Solution().subarraySum(nums = [1,1,1], k = 2)) #2
print(Solution().subarraySum(nums = [1], k = 0)) #0