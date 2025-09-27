#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occured = set(nums)
        ans = 0
        
        for num in occured:
            consequtive_len = 0
            # 連続数値開始地点
            if not num - 1 in occured:
                # 連続数値のカウント
                target_num = num
                while target_num + 1 in occured:
                    consequtive_len += 1
                    target_num += 1
                ans = max(ans, consequtive_len + 1)
        return ans
            

        
# @lc code=end

print("exp: 4" + " / " + str(Solution().longestConsecutive(nums = [100,4,200,1,3,2])))
print("exp: 9" + " / " + str(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])))
print("exp: 3" + " / " + str(Solution().longestConsecutive(nums = [1,0,1,2])))
print("exp: 0" + " / " + str(Solution().longestConsecutive(nums = [])))