#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
・部分問題
    ・現ノードは左右どちらかの子を持つか？
        ・Yes：再帰
        ・No：深さ更新

・例外
    ・ノードが存在しない(null)
    ・子を持たないノードしかない場合(rootのみ)

・状態
    ・深さの最小値
    ・現在の深さ

・状態遷移
    if not node.right and not node.left:
        depth = min(depth, 現在の深さ)
    if node.right:
        dfs(node.right)
    if node.left:
        dfs(node.left)
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = float('inf')
        def __dfs(node: TreeNode, curr_depth: int):
            nonlocal min_depth
            if not node.right and not node.left:
                min_depth = min(min_depth, curr_depth)
                return

            if node.right:
                __dfs(node.right, curr_depth+1)
            if node.left:
                __dfs(node.left, curr_depth+1)
            return
        
        if not root:
            return 0
        __dfs(root, 1)
        return min_depth

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
print(Solution().minDepth(tree1))  # 2

tree2 = build_tree([2,None,3,None,4,None,5,None,6])
print(Solution().minDepth(tree2))  # 5

tree3 = build_tree([])
print(Solution().minDepth(tree3))  # [0]

tree4 = build_tree([1])
print(Solution().minDepth(tree4))  # [1]