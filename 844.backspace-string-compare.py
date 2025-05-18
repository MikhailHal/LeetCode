#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for c in s:
            if c == '#':
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(c)

        for c in t:
            if c == '#':
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(c)
        
        return s_stack == t_stack
# @lc code=end
print(Solution().backspaceCompare(s = "y#fo##f", t = "y#f#o##f"))
