#
# @lc app=leetcode id=2351 lang=python3
#
# [2351] First Letter to Appear Twice
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for c in s:
            if c in dic:
                print(c)
                return c
            dic[c] = 0
# @lc code=end

Solution().repeatedCharacter("abcdd")