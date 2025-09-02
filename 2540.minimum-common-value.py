#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lc code=start
from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            while ptr1 < len(nums1) and nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            if ptr1 >= len(nums1):
                return -1

            while ptr2 < len(nums2) and nums2[ptr2] < nums1[ptr1]:
                ptr2 += 1
            if ptr2 >= len(nums2):
                return -1

            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
        return -1
        
# @lc code=end

print(Solution().getCommon([3,4,5], [1,1,2,5]))