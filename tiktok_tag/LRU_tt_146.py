class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

"""
这一题用到了double linked list，因为我们需要在O(1)时间内删除和添加节点,
然后用了dictionary 来存储key和对应的node，这样我们可以在O(1)时间内找到对应的node
Time complexity: O(1)
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # check capacity 
        if key in self.dict:
            old_node = self.dict[key]
            self.remove(old_node)
        
        new_node = ListNode(key, value)
        self.dict[key] = new_node
        self.add(new_node)

        if len(self.dict) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]

    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)