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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        prev = dummy_node
        current = head
        seen = set()

        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next
        return head

linked_list = create_linked_list([1,1,2,3,3])
print(Solution().deleteDuplicates(linked_list))