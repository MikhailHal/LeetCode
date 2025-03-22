#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for char in magazine:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        
        for char in ransomNote:
            if not char in dict:
                return False
            if dict[char] <= 0:
                return False
            else:
                dict[char] -= 1
        return True
# @lc code=end
