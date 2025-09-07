#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List
class Solution:
    def calcOperands(self, num1: int, num2: int, operand: str):
        if operand == '+':
            return num1 + num2
        elif operand == '-':
            return num1 - num2
        elif operand == '*':
            return num1 * num2
        elif operand == '/':
            return num1 / num2
 
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                b = stack.pop()
                a = stack.pop()
                calc_result = self.calcOperands(int(a), int(b), token)
                stack.append(calc_result)
            else:
                stack.append(token)
        return int(stack.pop())
# @lc code=end

print(Solution().evalRPN(["18"])) #18
print(Solution().evalRPN(["4","13","5","/","+"])) #6
print(Solution().evalRPN(["1"])) #1
print(Solution().evalRPN(["2","1","+","3","*"])) #9
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) #22