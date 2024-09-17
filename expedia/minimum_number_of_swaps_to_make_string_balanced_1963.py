class Solution:
    def minSwaps(self, s: str) -> int:
        # ]]] [[[

        """
        For every 2 pairs of square brackets, a swap will make them matched;
        If only 1 pair not matched, we need a swap.
        Therefore, we need at least (pairs + 1) / 2 swaps.
        """
        stack = []
        for c in s:
            if stack and c == ']':
                stack.pop()
            elif c == '[':
                stack.append(c)
        
        return (len(stack) + 1) // 2
