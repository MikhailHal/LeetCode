#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

"""
部分問題
・nums[i]に対する、targetを構成するための補数(complement)が存在するかどうか

状態
・補数インデックス辞書(キー：nums[i] / バリュー：i)

 漸化式
    if complement in seen:
        return [i, seen[complement]]
    seen[num] = i

例外
・numsのサイズが2の場合

"""
# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i
# @lc code=end

print(Solution().twoSum(nums = [2,7,11,15], target = 9))
print(Solution().twoSum(nums = [3,2,4], target = 6))
print(Solution().twoSum(nums = [3,3], target = 6))