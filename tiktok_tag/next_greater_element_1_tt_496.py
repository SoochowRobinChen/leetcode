class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        因为每个元素都是unique，所以可以用
        hash map 来存储nums2中每个元素的下一个更大的元素
        然后遍历nums1，直接查找hash map即可
        """
        lookup, stack = {}, []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            lookup[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])


        res = []
        for n in nums1:
            res.append(lookup[n])
        
        return res 
