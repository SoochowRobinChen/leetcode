class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        sec = 1
        while memory1 - sec >= 0 or memory2 - sec >= 0:
            if memory1 >= memory2:
                memory1 -= sec
            else:
                memory2 -= sec
            sec += 1
        
        return [sec, memory1, memory2]