class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1, freq2 = {}, {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1
        
        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1
        
        arr1 = sorted(list(freq1.values()))
        arr2 = sorted(list(freq2.values()))

        s1 = set(word1)
        s2 = set(word2)

        return len(word1) == len(word2) and s1 == s2 and arr1 == arr2