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
        # 復習のためコードは消しました。前の回答みたければGitHub見て
        pass

# @lc code=end
#print(Solution().removeNthFromEnd(listNodes, 2))
listNodes = make_linked_list([1,2,1])
#listNodes = make_linked_list([1,2,1,None])
print(Solution().isPalindrome(listNodes))