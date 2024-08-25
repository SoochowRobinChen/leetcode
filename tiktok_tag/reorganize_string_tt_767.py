class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in counter.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ''

        while max_heap or prev:

            if prev and not max_heap:
                return ''

            cnt, char = heappop(max_heap)
            res += char
            cnt += 1

            if prev:
                heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        
        return res 
    
    
    """
    freq = [0] * 26

        # Calculate the frequency of each character
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Find the character with the maximum frequency
        max_freq = 0
        letter = 0
        for i in range(26):
            if freq[i] > max_freq:
                max_freq = freq[i]
                letter = i

        # Edge case: if the most frequent character appears more than half the length of s, return ""
        if max_freq > (len(s) + 1) // 2:
            return ""

        # Reorganize the string
        result = [''] * len(s)
        idx = 0

        # Fill the result array with the most frequent character first, placed at even indexes
        while freq[letter] > 0:
            result[idx] = chr(ord('a') + letter)
            freq[letter] -= 1
            idx += 2

        # Fill the rest of the characters
        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):
                    idx = 1  # Move to the next odd index
                result[idx] = chr(ord('a') + i)
                freq[i] -= 1
                idx += 2

        return "".join(result)



    
    
    """