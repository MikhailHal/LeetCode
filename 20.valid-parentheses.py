#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
"""
部分問題
s[i]がopen bracketの場合 : スタックへプッシュして終わり
s[i]がclose bracketの場合：pop結果のブラケットが自身と対応しているかどうか

例外
popできない場合
close_bracketがない場合

状態
open bracketの管理

遷移処理(s[i]がopen bracket)
bracket_stack.push(s[i])

遷移処理(s[i]がclose bracket)
pop可能:
  bracket = bracket_stack.pop()
  自身と対応しているかどうか(関数)
  してなければreturn false

pop不可能:
  return false
  
"""
class Solution:
    def __isValidBracket(self, open_bracket: str, close_bracket: str) -> bool:
        if close_bracket == ")":
            return open_bracket == "("
        
        elif close_bracket == "}":
            return open_bracket == "{"
        
        elif close_bracket == "]":
            return open_bracket == "["
        
        else:
            return False

    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                bracket_stack.append(c)
                continue
            if len(bracket_stack) <= 0:
                return False
            open_bracket = bracket_stack.pop()
            if not self.__isValidBracket(open_bracket, c):
                return False
        return len(bracket_stack) <= 0

            
# @lc code=end

print(Solution().isValid("()")) # true
print(Solution().isValid("()[]{}")) # true
print(Solution().isValid("(]")) # false
print(Solution().isValid("]")) # false
print(Solution().isValid("(")) # false