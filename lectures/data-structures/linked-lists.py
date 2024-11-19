#SINGLY LINKED LISTS

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def append(self, data):
    new_node = Node(data) # Creating new node
    if not self.head: # if the list is empty
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node 