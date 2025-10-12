#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
"""
1.substructure
nums[i]時点で出現記録マップに値があるかどうか

2.state
・出現記録マップ(occurence_map)
・答え(ans)
・nums[i]時点での組み合わせ数
"""
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_map = dict()
        ans = 0
        for num in nums:
            if num in count_map:
                ans += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1
        return ans
# @lc code=end

Solution().numIdenticalPairs(nums = [1,2,3,1,1,3])
# 4

Solution().numIdenticalPairs(nums = [1,1,1,1])
# 6

Solution().numIdenticalPairs(nums = [1,2,3])
# 0

Solution().numIdenticalPairs(nums = [1])
# 0