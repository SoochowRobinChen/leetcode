"""
This file contains the knowledge related with deque in python.
Deque (Doubly Ended Queue) in python is implemented using the module "collections".
Deque is preferred over a list in the case when we need quicker append and pop operations
from both and ends of the queue. 
------------
append()
appendleft()
pop()
popleft()
len(deque) -> return length of deque
------------
"""


from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])

print(queue)
queue.append(4)
queue.appendleft(0)
print(queue)
queue.pop()
queue.popleft()
print(queue)