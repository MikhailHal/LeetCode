#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                top_char = stack.pop()
                if c != top_char:
                    stack.append(top_char)
                    stack.append(c)
        return ''.join(stack)
# @lc code=end

print(Solution().removeDuplicates("abab"))
print(Solution().removeDuplicates("abbaca"))
print(Solution().removeDuplicates("a"))
print(Solution().removeDuplicates("aa"))
print(Solution().removeDuplicates("azxxzy"))