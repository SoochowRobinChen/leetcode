class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s

        heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(heap)

        ans = []

        while heap:
            temp_items = []

            if len(heap) < k and -heap[0][0] > 1:
                return ''
            
            for _ in range(min(k, len(heap))):
                count, char = heappop(heap)
                ans.append(char)

                if -count > 1:
                    temp_items.append((count + 1, char))
            
            for item in temp_items:
                heappush(heap, item)
        
        return ''.join(ans)