#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       if not root:
           return None
       left = root.right
       right = root.left
       root.left = left
       root.right = right
       self.invertTree(root.left)
       self.invertTree(root.right)
       return root
        
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

#tree1 = build_tree([4,2,7,1,3,6,9])
#print(Solution().invertTree(tree1))  # [4,7,2,9,6,3,1]

tree2 = build_tree([2,1,3])
print(Solution().invertTree(tree2))  # [2,3,1]

tree3 = build_tree([])
print(Solution().invertTree(tree3))  # []