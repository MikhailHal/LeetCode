#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            level_size = len(queue)
            current_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val
                # 現在の層でやりたいこと
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # 結果使ってやりたいこと
            ans.append(current_sum / level_size)
        return ans
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
print(Solution().averageOfLevels(tree1))  # [3.00000,14.50000,11.00000]

tree2 = build_tree([3,9,20,15,7])
print(Solution().averageOfLevels(tree2))  # [3.00000,14.50000,11.00000]

tree3 = build_tree([1])
print(Solution().averageOfLevels(tree3))  # [1]