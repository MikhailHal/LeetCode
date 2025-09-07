#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                opened_bracket = stack.pop()
                if opened_bracket == '(' and c == ')':
                    continue
                elif opened_bracket == '[' and c == ']':
                    continue
                elif opened_bracket == '{' and c == '}':
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True
        
        
# @lc code=end
print(Solution().isValid("((")) # false
print(Solution().isValid("()[]")) # true
print(Solution().isValid("()")) # true
print(Solution().isValid("(]")) # false
print(Solution().isValid("(")) # false
print(Solution().isValid("[]")) # true
print(Solution().isValid("([])")) # true
print(Solution().isValid("([)]")) # false