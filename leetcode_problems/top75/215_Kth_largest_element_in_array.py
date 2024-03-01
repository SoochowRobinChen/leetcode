class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Heap data structure is mainly used to represent a priority queue. 
        In Python, it is available using the "heapq" module. The property of 
        this data structure in Python is that each time the smallest heap element 
        is popped(min-heap). Whenever elements are pushed or popped, heap structure
        is maintained. 
        ----------------
        heapq.heapify() -> O(n)
        heapq.heappush(iterable, element)
        heapq.heappop(iterable)
        when you push, pop element in the heap, the order is adjusted.
        """

        # use heap data structure
        heap = nums[:k]
        # O(n) -> build heap 
        heapq.heapify(heap)

        for element in nums[k:]:
            heapq.heappush(heap, element)
            heapq.heappop(heap)
        
        return heapq.heappop(heap)

        # quick selection .