#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumericStr = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        first = 0
        last = len(alphanumericStr) - 1
        while first < last:
            if alphanumericStr[first] != alphanumericStr[last]:
                return False
            first += 1
            last -= 1
        return True
# @lc code=end
