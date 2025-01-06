class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to act as the head of the new list
    dummy = ListNode()
    current = dummy

    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Append the remaining nodes of the non-empty list
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Example usage
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])

merged_list = mergeTwoLists(list1, list2)
printLinkedList(merged_list)
