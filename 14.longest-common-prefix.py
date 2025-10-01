#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        ans = ""
        for str in strs:
            min_len = min(min_len, len(str))

        for i in range(min_len):
            target_str = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != target_str:
                    return ans
            ans += target_str
        return ans
# @lc code=end

print(Solution().longestCommonPrefix(strs = ["cir","car"]))
# "c"

print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))
# "fl"

print(Solution().longestCommonPrefix(strs = ["dog","racecar","car"]))
# ""

print(Solution().longestCommonPrefix(strs = ["foower","foow","foight"]))
# "fo"