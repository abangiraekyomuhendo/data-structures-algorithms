# Data Structures and Algorithms Cheat Sheet

## 1. Data Structures

| **Data Structure** | **When to Use** | **Key Operations**                          | **Example**                                                                 |
|---------------------|-----------------|---------------------------------------------|-----------------------------------------------------------------------------|
| **Array**          | Fixed-size data | Access: \(O(1)\), Insert/Delete: \(O(n)\)   | Storing marks of students: `[90, 80, 70]`                                   |
| **Linked List**    | Dynamic size, frequent inserts | Insert/Delete: \(O(1)\), Access: \(O(n)\) | Train compartments: `Head → Node1 → Node2`                                 |
| **Stack**          | LIFO (last in, first out) | Push/Pop: \(O(1)\)                         | Browser back button: `['Page1', 'Page2']`                                   |
| **Queue**          | FIFO (first in, first out) | Enqueue/Dequeue: \(O(1)\)                 | Printer tasks: `['Task1', 'Task2']`                                         |
| **Hash Table (Dict)** | Fast lookups         | Access: \(O(1)\), Insert: \(O(1)\)         | Storing student grades: `{ 'Alice': 90, 'Bob': 80 }`                        |
| **Binary Tree**    | Hierarchical data | Insert/Search: \(O(\log n)\)               | File directories: Root → `Folder1`, `Folder2 → Subfolder`                  |
| **Graph**          | Networks         | Depends on representation (Adjacency list or matrix) | Social network: Users connected by edges.                                  |

## 2. Algorithm Categories

| **Category**            | **When to Use**                  | **Examples**                                                                 |
|--------------------------|----------------------------------|-----------------------------------------------------------------------------|
| **Sorting**             | Organize data                   | Bubble Sort, Quick Sort, Merge Sort                                         |
| **Searching**           | Find an item in data            | Linear Search (\(O(n)\)), Binary Search (\(O(\log n)\))                     |
| **Greedy Algorithms**   | Optimization problems           | Dijkstra’s Shortest Path, Huffman Encoding                                 |
| **Divide and Conquer**  | Break problem into smaller ones | Merge Sort, Quick Sort, Binary Search                                      |
| **Dynamic Programming** | Overlapping subproblems          | Fibonacci Sequence, Knapsack Problem                                       |
| **Graph Traversal**     | Explore nodes in a graph         | BFS (\(O(V+E)\)), DFS (\(O(V+E)\))                                         |

## 3. Time Complexity Table

| **Operation/Algorithm**         | **Best Case** | **Worst Case**    |
|----------------------------------|---------------|-------------------|
| **Access (Array)**              | \(O(1)\)      | \(O(1)\)          |
| **Search (Linear)**             | \(O(1)\)      | \(O(n)\)          |
| **Search (Binary)**             | \(O(1)\)      | \(O(\log n)\)     |
| **Sorting (Quick Sort)**        | \(O(n \log n)\)| \(O(n^2)\)        |
| **Sorting (Merge Sort)**        | \(O(n \log n)\)| \(O(n \log n)\)   |
| **Graph BFS/DFS**               | \(O(V+E)\)    | \(O(V+E)\)        |

## 4. Common Problems and Data Structure to Use

| **Problem Type**                  | **Best Data Structure** |
|-----------------------------------|--------------------------|
| **Need fast lookups by key**      | Hash Table (Dictionary)  |
| **Keep order, allow duplicates**  | List/Array               |
| **Hierarchical relationships**    | Binary Tree              |
| **Process items in order**        | Queue                   |
| **Undo/Redo operations**          | Stack                   |
| **Find shortest paths in graphs** | Graph + Dijkstra/DFS/BFS |

## 5. Example Code Snippets

### 1. Binary Search (Python)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
nums = [10, 20, 30, 40, 50]
print(binary_search(nums, 30))  # Output: 2






When to Use Each Algorithm:
Linear Search: Good for unsorted lists or when you don’t need efficiency.
Binary Search: Best for sorted lists; very efficient.
Bubble Sort, Selection Sort, Insertion Sort: Simple but inefficient for large lists (O(n^2)). They can be good for small or nearly sorted data.
Merge Sort: Efficient for large lists and guarantees O(n log n) time complexity.
Quick Sort: Very efficient on average for large datasets but needs to be carefully implemented to avoid worst-case performance.

