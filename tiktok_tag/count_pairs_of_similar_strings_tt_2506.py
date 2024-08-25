class Solution:
    def similarPairs(self, words: List[str]) -> int:
        """
        很巧妙计算pair的方法
        """

        freq = defaultdict(int)
        count = 0
        for curr_word in words:
            word = ''.join(sorted(set(curr_word)))
            count += freq[word]
            freq[word] += 1
        
        return count 