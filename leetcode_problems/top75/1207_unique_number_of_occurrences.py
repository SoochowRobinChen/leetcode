class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        # how to get keys() and values() in dict of python?
        return len(hashMap.keys()) == len(set(hashMap.values()))