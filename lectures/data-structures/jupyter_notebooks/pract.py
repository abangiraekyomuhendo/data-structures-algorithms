# 1. Data Structures and Operations

# (a) Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def display(self):
        return self.items

# Create a stack
stack = Stack()
# Push three integers onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
# Pop two integers from the stack
stack.pop()
stack.pop()
# Display the remaining elements in the stack
print(f"Remaining elements in the stack: {stack.display()}")

# (b) Queue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def display(self):
        return self.items

# Create a queue
queue = Queue()
# Add five names to the queue
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")
queue.enqueue("David")
queue.enqueue("Eve")
# Remove two names from the queue
queue.dequeue()
queue.dequeue()
# Display the remaining names in the queue
print(f"Remaining names in the queue: {queue.display()}")

# 2. Algorithm Analysis

# (a) Sum of the First `n` Natural Numbers
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = 10
print(f"Sum of the first {n} natural numbers: {sum_natural_numbers(n)}")
# Time complexity analysis: O(n)

# (b) Binary Search with Comparisons
def binary_search_with_comparisons(array, target):
    low = 0
    high = len(array) - 1
    comparisons = 0

    while low <= high:
        mid = (high + low) // 2
        comparisons += 1

        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid, comparisons

    return -1, comparisons

array = sorted([2, 3, 4, 10, 40])
target = 10

index, comparisons = binary_search_with_comparisons(array, target)
print(f"Element found at index: {index}, Number of comparisons: {comparisons}")

# 3. Recursion

# (a) Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = 4
print(f"Factorial of {n}: {factorial(n)}")
# Trace:
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 * factorial(0)
# factorial(0) = 1

# (b) Tower of Hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')

# 4. Searching and Sorting Algorithms

# (a) Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(f"Array after pass {i}: {array}")

array = [12, 11, 13, 5, 6, 7, 2, 3, 9, 1]
insertion_sort(array)

# (b) Bubble Sort with Swap Count
def bubble_sort_with_swaps(array):
    swap_count = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_count += 1
    return array, swap_count

array = [5, 1, 4, 2, 8]
sorted_array, swaps = bubble_sort_with_swaps(array)
print(f"Sorted array: {sorted_array}, Number of swaps: {swaps}")

# 5. Graphs

# (a) Adjacency Matrix
def create_adjacency_matrix(connections):
    nodes = sorted(set([x for conn in connections for x in conn]))
    size = len(nodes)
    index = {nodes[i]: i for i in range(size)}
    matrix = [[0] * size for _ in range(size)]

    for (start, end) in connections:
        i, j = index[start], index[end]
        matrix[i][j] = matrix[j][i] = 1

    return nodes, matrix

def print_adjacency_matrix(nodes, matrix):
    print(" ", " ".join(nodes))
    for i in range(len(nodes)):
        print(nodes[i], " ".join(map(str, matrix[i])))

connections = [('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'D')]
nodes, matrix = create_adjacency_matrix(connections)
print_adjacency_matrix(nodes, matrix)

# (b) Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start = 'A'

dfs_traversal = dfs(graph, start)
print(f"DFS Traversal Order: {dfs_traversal}")

# (c) Breadth-First Search (BFS)
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([node for node in graph[vertex] if node not in visited])
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start = 'A'

bfs_traversal = bfs(graph, start)
print(f"BFS Traversal Order: {bfs_traversal}")
