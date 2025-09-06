#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def make_linked_list(nums: list[int]) -> ListNode:
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        node = ListNode(num)
        curr.next = node
        curr = curr.next
    return head
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None
        curr = None

        # fast/slow使って中央部ノードを走査
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 反転開始位置ポインタセット
        if fast == None:
            curr = slow
        else:
            curr = slow.next

        # 後半部分を反転
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # 各リストの回文チェック
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

# @lc code=end
#print(Solution().removeNthFromEnd(listNodes, 2))
listNodes = make_linked_list([1,2,1])
#listNodes = make_linked_list([1,2,1,None])
print(Solution().isPalindrome(listNodes))