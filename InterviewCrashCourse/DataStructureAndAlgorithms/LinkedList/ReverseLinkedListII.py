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

"""
1→2→3→4→5
1→2←3←4→5
1→4→3→2→5
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = prefix_node = None
        current = head
        prefix_pos = 0

        # find a start point of reversal
        for _ in range(left-1):
            prefix_node = current
            current = current.next
            prefix_pos += 1
        
        # reverse all nodes from left to right
        for _ in range(left, right+1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node # it would be the suffix node
        
        # let's join all nodes as the reversed list yay yay!!! I'm gonna get into google no time!!
        suffix_node = next_node
        ans = head
        # join the prefix node and the reversed list
        if prefix_node:
            node = ans
            pos = 0
            while node:
                if pos == prefix_pos-1:
                    node.next = prev
                    break
                node = node.next
                pos += 1
        else:
            ans = prev
        
        if suffix_node:
            node = ans
            while node.next:
                node = node.next
            node.next = suffix_node
        
        return ans

#linked_list = create_linked_list([3,5,6])
#Solution().reverseBetween(linked_list, 1, 1)

linked_list = create_linked_list([4,4,-3,-2, 4])
Solution().reverseBetween(linked_list, 3, 3)

linked_list = create_linked_list([1,2,3,4,5])
Solution().reverseBetween(linked_list, 2, 4)