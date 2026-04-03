# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: ListNode) -> ListNode:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        odd = head
        even = even_head = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
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
    head = createLinkedList([1, 2, 3, 4, 5, 6, 7])
    printLinkedList(head)
    head = oddEvenList(head)
    printLinkedList(head)
