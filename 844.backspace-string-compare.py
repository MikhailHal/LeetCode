#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        s_skip = t_skip = 0

        while i >=0 or j >= 0:
            # find a valid character in s
            while i >= 0:
                if s[i] == '#':
                    i -= 1
                    s_skip += 1
                elif s_skip > 0:
                    i -= 1
                    s_skip -= 1
                else:
                    break

            # find a valid character in t
            while j >= 0:
                if t[j] == '#':
                    j -= 1
                    t_skip += 1
                elif t_skip > 0:
                    j -= 1
                    t_skip -= 1
                else:
                    break
        
            # if one string is exhausted
            if (i < 0) != (j < 0):
                return False
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            # decrement each index
            i -= 1
            j -= 1
        
        return True
# @lc code=end
print(Solution().backspaceCompare(s = "a##cab##", t = "a##c"))
