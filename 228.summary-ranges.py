#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
'''
1-部分問題
nums[i] == nums[i-1] + 1かどうか

2-状態
・範囲の先頭の値

'''
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rangeStartIndex = 0
        ans = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        for i in range(1,len(nums)):
            # 一つ前の値から1増えただけの場合かどうか
            if nums[i] == nums[i - 1] + 1:
                continue
            # 一つ前の値から2以上増えた場合
            # 答えに追加する範囲が複数ある場合
            if i - rangeStartIndex > 1:
                ans.append(f"{nums[rangeStartIndex]}->{nums[i - 1]}")
            # 答えに追加する範囲が1つのみの場合
            else:
                ans.append(str(nums[rangeStartIndex]))
            rangeStartIndex = i
        # 最終インデックスの処理
        if nums[len(nums) - 2] + 1 == nums[len(nums) - 1]:
            ans.append(f"{nums[rangeStartIndex]}->{nums[len(nums) - 1]}")
        else:
            ans.append(str(nums[len(nums) - 1]))
        return ans

        
# @lc code=end

print(''.join(Solution().summaryRanges(nums = [0,1,2])))
# ["0->2"]

print(''.join(Solution().summaryRanges(nums = [0,1,3])))
# ["0->1", "3"]

print(''.join(Solution().summaryRanges(nums = [0,2,3])))
# ["0", "2->3"]

print(''.join(Solution().summaryRanges(nums = [0,1,2,4,5,7])))
# ["0->2","4->5","7"]

print(''.join(Solution().summaryRanges(nums = [0,2,3,4,6,8,9])))
# ["0","2->4","6","8->9"]

print(''.join(Solution().summaryRanges(nums = [])))
# []

print(''.join(Solution().summaryRanges(nums = [1])))
# ["1"]