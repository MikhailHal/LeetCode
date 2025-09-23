#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occured_index_map = {}
        for i, num in enumerate(nums):
            if num in occured_index_map:
                prev_index = occured_index_map[num]
                if abs(occured_index_map[num] - i) <= k and nums[prev_index] == nums[i]:
                    return True
                else:
                    occured_index_map[num] = i
            else:
                occured_index_map[num] = i
        return False
# @lc code=end

print("exp: True" + " / " + str(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3)))
print("exp: True" + " / " + str(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1)))
print("exp: False" + " / " + str(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)))
print("exp: False" + " / " + str(Solution().containsNearbyDuplicate(nums = [1], k = 0)))