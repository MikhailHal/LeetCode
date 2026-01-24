#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
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
    ・現ノードと最も値の大きいノードと比較して最大値を取る
    ・現ノードと最も値の小さいノードと比較して最小値を取る
    ・子がいればdfs
・例外
    ・部分問題を破壊する例外はなし

・状態
    ・現ノードにおける最大値：int
    ・現ノードにおける最小値：int

・状態遷移
    path_max = max(path_max, node.val)
    path_min = min(path_min, node.val)
    ans = max(ans, path_max - path_min)
    if node.left:
        dfs(node.left, path_max, path_min)
    if node.right:
        dfs(node.right, path_max, path_min)

"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def __traversalNode(node: TreeNode, path_max: int, path_min: int):
            nonlocal ans
            path_max = max(path_max, node.val)
            path_min = min(path_min, node.val)
            ans = max(ans, path_max - path_min)
            if node.left:
                __traversalNode(node.left, path_max, path_min)
            if node.right:
                __traversalNode(node.right, path_max, path_min)
            return
        
        if root.left:
            __traversalNode(root.left, root.val, root.val)
        if root.right:
            __traversalNode(root.right, root.val, root.val)
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

tree1 = build_tree([8,3,10,1,6,None,14,None,None,4,7,13])
print(Solution().maxAncestorDiff(tree1))  # 7

tree2 = build_tree([1,None,2,None,0,3])
print(Solution().maxAncestorDiff(tree2))  # 3

tree3 = build_tree([1,None,2])
print(Solution().maxAncestorDiff(tree3))  # 1