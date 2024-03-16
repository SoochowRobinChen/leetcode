class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # construct diff list
        diff = [0] * length

        for update in updates:
            start = update[0]
            end = update[1]
            val = update[2]

            diff[start] += val
            # pay attention to this statement 
            if end + 1 < length:
                diff[end + 1] -= val
        
        res = [diff[0]]

        for i in range(1, length):
            res.append(res[-1] + diff[i])
        
        return res
    
