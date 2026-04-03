# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: ListNode) -> ListNode:
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Tortoise and Hare Algorithm for finding midpoint
    if head.next == None:
        return None
    
    prev = None
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next

    return head


def createLinkedList(arr: list) -> ListNode:
    head = prev = curr = None
    for num in arr:
        curr = ListNode(num)
        if not head:
            head = curr
        else:
            prev.next = curr
        prev = curr
    return head

def printLinkedList(head: ListNode):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(' -> '.join(elements))


if __name__ == "__main__":
    head = createLinkedList([0, 1, 2, 3, 4, 5, 6])
    printLinkedList(head)
    head = deleteMiddle(head)
    printLinkedList(head)

    
