#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans = False
    def check_is_exits_target(self, node: TreeNode, currentSum: int, targetSum: int):
        if not node:
            return
        currentSum += node.val
        if currentSum == targetSum and not node.left and not node.right:
            self.ans = True
            return
        self.check_is_exits_target(node.left, currentSum, targetSum)
        self.check_is_exits_target(node.right, currentSum, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        self.check_is_exits_target(root, 0, targetSum)
        return self.ans
        
# @lc code=end

# テスト用のヘルパー関数
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

tree1 = build_tree([5,4,2])
print(Solution().hasPathSum(tree1, 9))  # true

tree2 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
print(Solution().hasPathSum(tree2, 22))  # true

tree3 = build_tree([1,2,3])
print(Solution().hasPathSum(tree3, 5))  # false

tree4 = build_tree([])
print(Solution().hasPathSum(tree4, -1000))  # false

tree5 = build_tree([1,2,3])
print(Solution().hasPathSum(tree5, 1))  # false

tree6 = build_tree([1])
print(Solution().hasPathSum(tree6, 1))  # true

tree7 = build_tree([1,2,3])
print(Solution().hasPathSum(tree7, 1))  # false