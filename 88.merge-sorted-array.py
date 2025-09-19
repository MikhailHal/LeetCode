#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
# @lc code=end

Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# [1,2,2,3,5,6]

Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0)
# [1]

Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
# [1]