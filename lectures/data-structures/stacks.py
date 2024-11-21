#LIFO data structure where you keep on pushing the elements and when you pop, it pops the last element that you pushed
#Push/pop is an O(1) - constant time
# to search an element in a stack by value, it will be O(n) - linear time

#Use cases for stack
# - Functin calling in any programming language is managed by stack. - Undo (Ctrl+Z) functionality in any editor uses stack to track down last set of operations


#class: list, collections.deque, queue.LifoQueue


# stk = deque()
# stk.append(5)
# stk.append(9)
# stk.pop() #returns 89

s = []
s.append('First')
s.append('Second')
s.append('Third')
s.append('Fourth')

#to get the last (so fourth)