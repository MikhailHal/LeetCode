#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        ans = ""
        isFirstOccurrence = True
        for right in range(len(word)):
            ans += word[right]
            if word[right] == ch and isFirstOccurrence:
                ans = word[left:right+1][::-1]
                isFirstOccurrence = False
        return ans

# @lc code=end

print(Solution().reversePrefix("bba", "b"))