#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0
        if not s:
            return True
        if not t:
            return False
        for i in range(0, len(t)):
            if t[i] == s[sPtr]:
                sPtr += 1
            if sPtr >= len(s):
                return True
        return False
# @lc code=end
