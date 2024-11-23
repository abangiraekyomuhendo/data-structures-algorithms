#SINGLY LINKED LISTS

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)  # Creating new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Make the new node the head
            return
        current = self.head  # Start at the first node
        while current.next:  # Move to the last node
            current = current.next
        current.next = new_node  # Link the new node

    # Display the list
    def display(self):
        current = self.head  # Start at the head
        while current:
            print(current.data, end=" -> ")  # Print the data
            current = current.next  # Move to the next node
        print("None")  # End of the list

    # Searching linked lists
    def search(self, target):
        current = self.head  # Start at the head
        while current:  # Loop through all the nodes in the list
            if current.data == target:  # If the target is found
                return current  # Return the current node
            current = current.next  # Move to the next node
        return None  # If the target is not found, return None


# Create and use the LinkedList
ll = LinkedList()  # Create an empty linked list
ll.append(10)      # Add the first node with data 10
ll.append(20)      # Add another node with data 20
ll.append(30)      # Add another node with data 30

ll.display()       # Call the display() method

# Searching for a value in the list
result = ll.search(20)  # Set the target here
if result:
    print(f"Found: {result.data}")
else:
    print("Not found")