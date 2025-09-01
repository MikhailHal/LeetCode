#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 1
        ans = ""
        
        while right <= len(s):
            if right >= len(s):
                ans += s[left:right][::-1]
                return ans
            
            if s[right] == " ":
                ans += s[left:right][::-1] + " "
                left = right + 1
                right = left + 1
                continue
            right += 1
        return ans

# @lc code=end

print(Solution().reverseWords("I love u"))
print(Solution().reverseWords("Let's take LeetCode contest"))
print(Solution().reverseWords("ab"))