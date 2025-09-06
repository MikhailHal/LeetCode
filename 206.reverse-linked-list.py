#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# LinkedList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LinkedListの生成
from typing import Optional
def create_linked_list(elements) -> Optional[ListNode]:
    if not elements:
        return None
    
    head = ListNode(elements[0])
    current = head

    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 復習のためコードは消しました。前の回答みたければGitHub見て
        pass
# @lc code=end
node_list = create_linked_list([1,2,3])
print(Solution().reverseList(node_list))