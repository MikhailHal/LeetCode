#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
        
        self.dfs(node.left)
        self.ans.append(node.val)
        self.dfs(node.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
print(Solution().inorderTraversal(tree1))  # [1,3,2]

tree2 = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
print(Solution().inorderTraversal(tree2))  # [4,2,6,5,7,1,3,9,8]

tree3 = build_tree([])
print(Solution().inorderTraversal(tree3))  # []

tree4 = build_tree([1])
print(Solution().inorderTraversal(tree4))  # [1]