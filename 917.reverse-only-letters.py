#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        ans = list(s)

        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while right > left and not s[right].isalpha():
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)
# @lc code=end

print(Solution().reverseOnlyLetters("ab-cd"))