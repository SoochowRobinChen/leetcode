class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        not_swap, swap = 0, 1
        for i in range(1, n):
            c1 = nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]
            c2 = nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]

            if c1 and c2:
                t = min(not_swap, swap)
                not_swap, swap = t, t + 1
            elif c1:
                swap += 1
            elif c2:
                not_swap, swap = swap, not_swap + 1

        return min(not_swap, swap) 