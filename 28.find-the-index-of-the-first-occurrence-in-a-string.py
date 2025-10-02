#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle) - 1
        while right < len(haystack):
            sub_str = haystack[left:right+1]
            if sub_str == needle:
                return left
            else:
                left += 1
                right += 1
        return -1
# @lc code=end

print(str(Solution().strStr(haystack = "sadbutsad", needle = "sad")))
# 0

print(str(Solution().strStr(haystack = "leetcode", needle = "leeto")))
# -1

print(str(Solution().strStr(haystack = "l", needle = "l")))
# 0

print(str(Solution().strStr(haystack = "l", needle = "ll")))
# -1