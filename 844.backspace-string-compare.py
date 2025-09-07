#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_c = []
        stack_t = []
        for c in s:
            if c != '#':
                stack_c.append(c)
            else:
                if stack_c:
                    stack_c.pop()
        
        for c in t:
            if c != '#':
                stack_t.append(c)
            else:
                if stack_t:
                    stack_t.pop()
        
        return ''.join(stack_c) == ''.join(stack_t)
# @lc code=end
print(Solution().backspaceCompare(s = "a#c", t = "b")) # true
print(Solution().backspaceCompare(s = "ab#c", t = "ad#c")) # true
print(Solution().backspaceCompare(s = "a#b", t = "a#b")) # true
print(Solution().backspaceCompare(s = "#", t = "#")) # true
print(Solution().backspaceCompare(s = "a#", t = "b")) # false
print(Solution().backspaceCompare(s = "a", t = "b#")) # false
