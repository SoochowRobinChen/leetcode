class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1, nums2 = version1.split('.'), version2.split('.')

        # 补0思维，如果两个版本号长度不一样，那么短的版本号后面补0
        for i in range(max(len(nums1), len(nums2))):
            p1 = int(nums1[i]) if i < len(nums1) else 0
            p2 = int(nums2[i]) if i < len(nums2) else 0

            if p1 != p2:
                return 1 if p1 > p2 else -1
        
        return 0