# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists 'list1' and 'list2'.
# Merge the two lists into one sorted list. The list should be made by splicing together
# the nodes of the first two lists.
# Return the head of the merged linked list.

from typing import List, Optional

# Optional type is used to enable "None" values
# ListNode is a node in linked list. 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def create_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()              # defaults with val=0
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:   # if list1 item is bigger than list2 item
                cur.next = list2        # list2 item will be the next item to compare, also implicitly means we keep the list1 item 
                list2 = list2.next      # done comparing, so we move to next item of list2

            else:                       # if list2 item is bigger than list1 item
                cur.next = list1        # list1 item will be the next item to compare, also implicitly means we keep the list2 item
                list1 = list1.next      # done comparing, so we move to next item of lists1
            
            cur = cur.next              # all item compared? time to check for next list in ListNode

        if list1:
            cur.next = list1            # if list1 still exist, go traverse
        else:
            cur.next = list2            # if list2 still exist, go traverse
            
        return dummy.next               # return real merged node, if only 'dummy' it will return pointer
    
if __name__ == "__main__":
    solution = Solution()

    list1 = create_linkedlist([1,2,4])
    list2 = create_linkedlist([2,3,4])
    result = solution.mergeTwoLists(list1, list2)
    print_linked_list(result)
