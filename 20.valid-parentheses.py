#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brancketMap = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        if len(s) <= 1:
            return False

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                
                if brancketMap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
                
        if len(stack) <= 0:
            return True
        else:
            return False
        
        
# @lc code=end
print(Solution().isValid("()"))
