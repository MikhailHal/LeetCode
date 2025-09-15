#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 復習のためコードは消しました。前の回答みたければGitHub見て
        pass

# @lc code=end
listNodes = make_linked_list([1,2])
print(Solution().removeNthFromEnd(listNodes, 2))
listNodes = make_linked_list([1,2,3,4,5])
print(Solution().removeNthFromEnd(listNodes, 1))
listNodes = make_linked_list([1,2,3,4,5])
print(Solution().removeNthFromEnd(listNodes, 2))
listNodes = make_linked_list([1,2,3,4])
print(Solution().removeNthFromEnd(listNodes, 2))