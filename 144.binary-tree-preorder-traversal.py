#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    ans = []
    def dfs(self, node: TreeNode):
        if not node:
            return
        self.ans.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        if root:
            self.dfs(root)
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

tree1 = build_tree([1,None,2,3])
print(Solution().preorderTraversal(tree1))  # [1,2,3]

tree2 = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
print(Solution().preorderTraversal(tree2))  # [1,2,4,5,6,7,3,8,9]

tree3 = build_tree([])
print(Solution().preorderTraversal(tree3))  # []

tree4 = build_tree([1])
print(Solution().preorderTraversal(tree4))  # [1]