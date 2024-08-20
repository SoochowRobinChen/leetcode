class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def find_common_prefix(a, b):
            length = min(len(a), len(b))
            res = 0
            for i in range(length):
                if a[i] == b[i]:
                    res += 1
                else:
                    break
            return res
        

        list1 = [str(a) for a in arr1]
        list2 = [str(a) for a in arr2]

        list1.sort()
        list2.sort()
        ans = 0

        for i in range(len(list2)):
            idx = bisect_left(list1, list2[i])

            if idx < len(list1):
                ans = max(ans, find_common_prefix(list1[idx], list2[i]))
            if idx > 0:
                ans = max(ans, find_common_prefix(list1[idx - 1], list2[i]))
        
        return ans 