#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
from typing import Optional
from math import ceil
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeIndex = 0
        tempNodeList = []
        currentNode = head
        while True:
            tempNodeList.append(currentNode)
            if currentNode.next == None:
                break
            else:
                currentNode = currentNode.next
                nodeIndex += 1
        return tempNodeList[ceil(nodeIndex/2)]
# @lc code=end
