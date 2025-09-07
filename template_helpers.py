"""
LeetCode Helper Functions Template
データ構造変換用のテンプレート集
"""

from collections import deque
from typing import List, Optional

# ============= Tree =============

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List) -> Optional[TreeNode]:
    """
    配列からTreeNodeを構築
    [3,9,20,None,None,15,7] → Tree構造
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def print_tree(root: TreeNode, level=0, prefix="Root: "):
    """
    Treeを視覚的に表示
    """
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# ============= Linked List =============

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

def print_linked_list(head: ListNode) -> str:
    """
    LinkedListを文字列として表示
    1->2->3->4->5
    """
    result = []
    current = head
    
    while current:
        result.append(str(current.val))
        current = current.next
    
    return " -> ".join(result)

def linked_list_to_array(head: ListNode) -> List:
    """
    LinkedListを配列に変換（検証用）
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

# ============= 使用例 =============

if __name__ == "__main__":
    # Tree例
    print("=== Tree Example ===")
    tree_values = [3, 9, 20, None, None, 15, 7]
    tree = build_tree(tree_values)
    print_tree(tree)
    
    print("\n=== Linked List Example ===")
    # LinkedList例
    list_values = [1, 2, 3, 4, 5]
    linked_list = build_linked_list(list_values)
    print(print_linked_list(linked_list))
    print("Array:", linked_list_to_array(linked_list))