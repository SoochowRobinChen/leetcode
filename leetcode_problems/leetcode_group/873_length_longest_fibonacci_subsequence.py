class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        S = set(arr)
        ans = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                x, y = arr[j], arr[i] + arr[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)

        return ans if ans >= 3 else 0