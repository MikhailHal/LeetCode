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
        count = 0
        prev = None
        curr = None
        while fast and fast.next:
            # Noneが入る可能性あり
            fast = fast.next.next
            slow = slow.next
            count += 1
        # 偶奇で反転開始位置ポインタが異なる
        if 

# @lc code=end
#print(Solution().removeNthFromEnd(listNodes, 2))
listNodes = make_linked_list([1,2,2,1])
listNodes = make_linked_list([1,2,1])
print(Solution().isPalindrome(listNodes))