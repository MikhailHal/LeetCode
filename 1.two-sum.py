#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

"""
部分問題
・nums[i]に対する補数(complement)が、過去に出現したか？

状態（最小化を意識）
・{数値: index} の辞書1つ
・補数は保存不要（target - num で都度計算できる）

状態遷移
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i  # 先にチェック、後で追加

境界・例外（部分問題が壊れるケース）
・同じ要素を2回使う → 「先にチェック、後で追加」の順序で回避
・解なし → 問題の制約で必ず1つ存在が保証

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