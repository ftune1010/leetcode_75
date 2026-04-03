# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        previous_node = None
        current_node = slow
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        max_sum = 0
        while previous_node:
            max_sum = max(max_sum, previous_node.val + head.val)
            previous_node =  previous_node.next
            head = head.next
        return max_sum

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
    head = createLinkedList([1, 2, 3, 4, 5, 6, 7, 20])
    printLinkedList(head)
    print(pairSum(head))

    
