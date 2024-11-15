##### Big O Notation 
Big O notation is a way of describing how the time or space requirements of an algorithm grow as the input size increases. Big O notation gives us an idea of how fast or an algorithm, especially when dealing with large amounts of data. 

###### Some Big O notations:
1. O(1) - Constant Time
   - no matter how bug the input is, the time it takes doesn't change
   - for example, looking at the first item in a list. It's just one step, regardless of how many items are below it. So it will be constant at all times. 
2. O(log n) - Logarithmic Time 
   - The time grows slowly even as the input size grows large. 
   - For example, binary search where you repeatedly split a sorted list in half to find an item. 
3. O(n) - Linear Time 
   - The time grows directly in proportion to the input size
   - For example 