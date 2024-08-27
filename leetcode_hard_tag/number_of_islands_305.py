class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # still use union find problem 
        res = []

        parent = {}
        # set the default value is 1
        rank = defaultdict(lambda: 1)

        def find(node):
            while node != parent[node]:
                node = parent[parent[node]]
            return node
        
        def union(node1, node2):
            node1_root = find(node1)
            node2_root = find(node2)

            if node1_root == node2_root:
                return False
            
            if rank[node1_root] > rank[node2_root]:
                parent[node2_root] = node1_root
                rank[node1_root] += rank[node2_root]
            else:
                parent[node1_root] = node2_root
                rank[node2_root] += rank[node1_root]

            return True

        count = 0

        """
        想清楚，如果一个新加入的点，肯定先加1，
        然后它的四周，如果已经有加入的点，那么就要union，而且count要减1
        3 个 点 加入一个新的点，变成1个的话，那就是 + 1 - 3 -> 原来3块，现在变成1块
        """
        for (r, c) in positions:
            if (r, c) not in parent:
                parent[(r, c)] = (r, c)
                count += 1
            
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in parent:
                    if union((r, c), (nr, nc)):
                        count -= 1
            
            res.append(count)
        
        return res 
