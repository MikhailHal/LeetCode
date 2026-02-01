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
・部分問題(main)
    ・dfs呼ぶだけ
・部分問題(dfs)
    目的：時点における最大差を返却
    引数：時点での最大ノード値int、時点での最小ノード値int、node
    ・最大/最小値の更新を行う
    ・最大差を求める
    ・左右の子それぞれいればdfsを呼ぶ
    ・現時点での最大差/左右の子の結果の中で最も大きい結果を返却

・例外
    部分問題を壊す例外はなし

・状態
    ・max_node_val: int
    ・min_node_val: int
    ・diff: int

・遷移

"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def __dfs(max_node_val: int, min_node_val: int, node: TreeNode):
            max_node_val = max(max_node_val, node.val)
            min_node_val = min(min_node_val, node.val)
            diff = abs(max_node_val - min_node_val)
            if node.left:
                diff = max(diff, __dfs(max_node_val, min_node_val, node.left))
            if node.right:
                diff = max(diff, __dfs(max_node_val, min_node_val, node.right))
            return diff
        return __dfs(root.val, root.val, root)
        
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