#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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

"""
・部分問題(本流)
    ・rootが空の場合は終了
    ・queue初期化
    ・出力リストへ追加
    ・bfs実施

・部分問題(bfs)
    目的：現階層のノードの全処理および次階層ノードの追加
    引数：現ノード(node)
    ・キューにノードが存在する間下記を実施
    ・キューからポップして現層のノードを全て保持
    ・そのノードの値を全てアウトプットに追加しつつ次の階層のノードをキューする
    ・最後にもう一度bfs

・例外
    ・二分木が空
    ・二分木が親のみ

・状態
    ・出力リスト(output_list)：List[List[int]]

・状態遷移
    node = queue.pop()
    curr_level_output = []
    if node.left:
        curr_level_output.append(node.left.val)
        queue.append(node.left)
    if node.right:
        curr_level_output.append(node.right.val)
        queue.append(node.right)
    output_lits.append(curr_level_output)


"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: deque
        ans: List[List[int]] = []
        def __bfs():
            nonlocal queue, ans
            while queue:
                level_size = len(queue)
                level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(level)
            return
        
        if not root:
            return []
        queue = deque([root])
        __bfs()
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

# テストケース
tree1 = build_tree([3,9,20,None,None,15,7])
print(Solution().levelOrder(tree1))  # [[3],[9,20],[15,7]]

tree2 = build_tree([1])
print(Solution().levelOrder(tree2))  # [[1]]

tree3 = build_tree([])
print(Solution().levelOrder(tree3))  # []

tree4 = build_tree([1,2,3,4,None,5,None])
print(Solution().levelOrder(tree4))  # [[1], [2,3], [4,5]]