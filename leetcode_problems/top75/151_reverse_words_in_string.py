class Solution:
    def reverseWords(self, s: str) -> str:

        """
        Use split() method is to use python built in method
        and how can we handle this in place?
        Time complexity is O(n)
        Space complexity is O(n)


        
        # use split method, it will remove white space directly 
        words = s.split()

        # reverse the list of words
        reversed_words = words[::-1]

        # join the reversed words with spaces
        reversed_string = ' '.join(reversed_words)

        return reversed_string

        """


class Solution:
    def trim_spaces(self, s):
        left, right = 0, len(s) - 1

        # remove leading space
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove tailling space
        while left <= right and s[right] == ' ':
            right -= 1

        # reduce multiple space into one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(' ')
            left += 1
        
        return output
    
    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    
    def reverse_each_word(self, l):
        n = len(l)
        start, end = 0, 0

        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            
            self.reverse(l, start, end - 1)

            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # 1. remove leading and tailing space, reduce multiple space into one
        l = self.trim_spaces(s)
        # 2. reverse whole string 
        self.reverse(l, 0, len(l) - 1)
        # 3. reverse each word
        self.reverse_each_word(l)

        return ''.join(l) 