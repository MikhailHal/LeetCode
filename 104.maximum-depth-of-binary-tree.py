#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def dfs(self, node: TreeNode) -> int:
        l_depth = r_depth = 0
        if not node:
            return 0
        
        l_depth += self.dfs(node.left)
        r_depth += self.dfs(node.right)
        return max(l_depth, r_depth) + 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
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

tree1 = build_tree([3,9,20,None,None,15,7])
print(Solution().maxDepth(tree1))  # 3

tree2 = build_tree([1,None,2])
print(Solution().maxDepth(tree2))  # 2