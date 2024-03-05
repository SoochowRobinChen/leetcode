class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 1. sort the potions
        potions.sort()
        n, m = len(spells), len(potions)
        pairs = [0] * n 
        # 2. BS -> find minimum index of potions
        for i in range(n):
            left, right = 0, m - 1
            spell = spells[i]

            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left

        # 3. construct pairs 
        return pairs