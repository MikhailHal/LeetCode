#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

# @lc code=end

print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("ab", "eidbaoooo"))
print(Solution().checkInclusion("abo", "eidbaoooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
print(Solution().checkInclusion("a", "a"))
print(Solution().checkInclusion("a", "b"))
print(Solution().checkInclusion("aa", "b"))