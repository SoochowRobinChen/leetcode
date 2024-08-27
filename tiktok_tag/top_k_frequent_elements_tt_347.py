class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        min_heap = []

        for key, value in counter.items():
            heappush(min_heap, (-value, key))
        
        res = []

        while len(res) < k:
            _, key = heappop(min_heap)
            res.append(key)
        
        return res 