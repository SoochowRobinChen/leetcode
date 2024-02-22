"""
Heap data structure is mainly used to represent a priority queue. 
In Python, it is available using the "heapq" module. The property of 
this data structure in Python is that each time the smallest heap element 
is popped(min-heap). Whenever elements are pushed or popped, heap structure
is maintained. 
----------------
heapq.heapify()
heapq.heappush(iterable, element)
heapq.heappop(iterable)
when you push, pop element in the heap, the order is adjusted.
"""
import heapq

# initializing list
li = [5, 7, 9, 1, 3]
# using heapify to convert list into heap
heapq.heapify(li)
print("The created heap is " , list(li))
# The created heap is  [1, 3, 9, 7, 5]