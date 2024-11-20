#SINGLY LINKED LISTS

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data) # Creating new node
        if not self.head: # if the list is empty
            self.head = new_node # make the new node the head
            return
        current = self.head #start at the first node
        while current.next: # move to the last node
            current = current.next
        current.next = new_node # link the new node


    #display the list
    def display(self):
        current = self.head #start at the head
        while current:
            print(current.data, end="->") #print the data
            current = current.next #move to the next node
        print("None") #end of the list

# Create and use the LinkedList
ll = LinkedList()  # Create an empty linked list
ll.append(10)      # Add the first node with data 10
ll.append(20)      # Add another node with data 20
ll.append(30)      # Add another node with data 30

ll.display()       # Call the display() method
