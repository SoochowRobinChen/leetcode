class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def left_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            
            if left < 0 or left >= len(nums):
                return -1
            
            return left if nums[left] == target else -1
        
        def right_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            
            if left - 1 < 0 or left - 1 >= len(nums):
                return -1
            
            return left - 1 if nums[left - 1] == target else -1