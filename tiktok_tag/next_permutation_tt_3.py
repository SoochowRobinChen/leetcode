class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = 0
        for i in range(N - 1, -1, -1):
            if nums[i] > nums[i-1]:
                pivot = i
                break
            # 4, 3, 2, 1 
        if pivot == 0:
            nums.sort()
            return 
        
        swap = N - 1
        while nums[swap] <= nums[pivot - 1]:
            swap -= 1

        nums[pivot - 1], nums[swap] = nums[swap], nums[pivot - 1]

        nums[pivot:] = reversed(nums[pivot:])