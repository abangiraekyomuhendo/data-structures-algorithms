# Linear Search
def linear_search(array, target):
    # Iterate through each element in the array
    for index in range(len(array)):
        # If the element is found, return its index
        if array[index] == target:
            return index
    # If the element is not found, return -1
    return -1

array = [400, 300, 900, 1000]
target = 900

result = linear_search(array, target)
print(f"The element is at index: {result}")

# Binary Search
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        # Check if the target is present at mid
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

array = sorted([400, 300, 900, 1000])
target = 900

result = binary_search(array, target)
print(f"The element is at index: {result}")

# Selection Sort
def selection_sort(array):
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

array = [400, 300, 900, 1000]

selection_sort(array)

print(f"The order is: ", array)

# Insertion Sort
def insertion_sort(array):
    # Traverse through 1 to len(array)
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of array[0..i-1], that are greater than key, to one position ahead
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

array = [400, 300, 900, 1000]

insertion_sort(array)

print(f"The order is: ", array)

# Merge Sort
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

array = [400, 300, 900, 1000]

merge_sort(array)

print(f"The order is: ", array)

# Quick Sort
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

array = [400, 300, 900, 1000]

array = quick_sort(array)

print(f"The order is: ", array)

# Graph Traversal - BFS (Breadth-First Search)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
start = 'A'

visited = bfs(graph, start)
print(f"Nodes visited in BFS order: {visited}")

# Graph Traversal - DFS (Depth-First Search)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
start = 'A'

visited = dfs(graph, start)
print(f"Nodes visited in DFS order: {visited}")

# Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(400)
stack.push(300)
stack.push(900)

print(f"Stack items: {[stack.pop() for _ in range(stack.size())]}")

# Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(400)
queue.enqueue(300)
queue.enqueue(900)

print(f"Queue items: {[queue.dequeue() for _ in range(queue.size())]}")
