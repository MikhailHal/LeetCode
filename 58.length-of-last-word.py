#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        s = s[::-1]
        is_already_occured_alpha = False
        for c in s:
            if c != " ":
                is_already_occured_alpha = True
                ans += 1
            else:
                if not is_already_occured_alpha:
                    continue
                break
        return ans

# @lc code=end

print(str(Solution().lengthOfLastWord(s = "Hello World")))
# 5

print(str(Solution().lengthOfLastWord(s = "   fly me   to   the moon  ")))
# 4

print(str(Solution().lengthOfLastWord(s = "luffy is still joyboy")))
# 6

print(str(Solution().lengthOfLastWord(s = "l")))
# 1