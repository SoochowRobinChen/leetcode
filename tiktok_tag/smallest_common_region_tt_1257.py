class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # build map from child -> parent 
        # traverse region1 add path to set

        # O(N)
        parent_map = defaultdict(str)

        for region in regions:
            parent = region[0]
            for child in region[1:]:
                parent_map[child] = parent
        
        ancestor = set()

        while region1:
            ancestor.add(region1)
            region1 = parent_map[region1]
        
        while region2 not in ancestor:
            region2 = parent_map[region2]

        return region2