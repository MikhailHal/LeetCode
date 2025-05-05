# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

def create_linked_list(elements) -> Optional[ListNode]:
    if not elements:
        return None
    
    head = ListNode(elements[0])
    current = head

    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

listNode = create_linked_list([1,2,3,4,5])
print(Solution().middleNode(listNode))