#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
"""
1.部分問題
ith時点におけるslowポインタの指すノードとfastポインタの指すノードが一致するかどうか。
もしfast.next.nextまたはslow.nextがなければfalse。

2.状態管理
fast = fast.next.next
slow = slow.next
fast: 常に2倍の速度で進行
slow: 常に等倍の速度で進行

"""
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values: List) -> Optional[ListNode]:
    """
    配列からLinkedListを構築
    [1,2,3,4,5] → 1->2->3->4->5
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        if not head or not fast.next:
            return False

        while fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False
        
# @lc code=end

nodes = build_linked_list([3,2,0,-4])
Solution().hasCycle(nodes)
# true

nodes = build_linked_list([1,2])
Solution().hasCycle(nodes)
# true

nodes = build_linked_list([1])
Solution().hasCycle(nodes)
# false

'''
f:3,0,2,-4
s:3,2,0,-4
'''