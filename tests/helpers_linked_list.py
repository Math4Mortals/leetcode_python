from solutions.common.linked_list import ListNode

def build_linked_list(values: list[int]) -> ListNode | None:
    head = ListNode(0)
    tail = head
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return head.next

def to_list(head: ListNode | None) -> list[int]:
    output = []
    curr = head
    while curr:
        output.append(curr.val)
        curr = curr.next
    return output
