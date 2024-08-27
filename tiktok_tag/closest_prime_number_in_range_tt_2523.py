class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for _ in range(right + 1)]
        p = 2
        prime[1] = False
        while p * p < right + 1:
            if prime[p] == True:
                for i in range(p * p, right + 1, p):
                    prime[i] = False
            
            p += 1
        

        res = [-1, -1]
        best = float('inf')
        last = -1

        for i in range(left, right + 1):
            if not prime[i]: continue
            if last > 0 and i - last < best:
                res = [last, i]
                best = i - last
            last = i
        
        return res 