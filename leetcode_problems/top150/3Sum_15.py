class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list
        nums.sort()
        res = []

        def two_sum(i, res):
            start, end = i + 1, len(nums) - 1

            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                if curr_sum == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    """
                    要想清楚还要remove two_sum里面的duplicates
                    """
                    # remove duplicates 
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                elif curr_sum > 0:
                    end -= 1
                elif curr_sum < 0:
                    start += 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                two_sum(i, res)
        
        return res
    