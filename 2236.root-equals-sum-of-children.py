#
# @lc app=leetcode id=2236 lang=python3
#
# [2236] Root Equals Sum of Children
#

# @lc code=start
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return True if root.left.val + root.right.val == root.val else False
# @lc code=end
