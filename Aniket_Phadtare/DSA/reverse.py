class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linkedlist(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original Linked List:")
display(head)

head = reverse_linkedlist(head)

print("Reversed Linked List:")
display(head)

          