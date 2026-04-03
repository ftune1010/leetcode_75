# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_node = head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node


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
    head = createLinkedList([0, 1, 2, 4])
    printLinkedList(head)
    head = reverseList(head)
    printLinkedList(head)

    
