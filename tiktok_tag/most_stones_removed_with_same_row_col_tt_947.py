class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, x, y):
        p_x, p_y = self.find(x), self.find(y)
        if p_x == p_y:
            return False
        
        if self.rank[p_x] > self.rank[p_y]:
            self.parent[p_y] = p_x
            self.rank[p_x] += self.rank[p_y]
        else:
            self.parent[p_x] = p_y
            self.rank[p_y] += self.rank[p_x]

        self.count -= 1

        return True
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[self.parent[x]]
        
        return x 
    
    def get_count(self):
        return self.count

"""
用Union Find来解决这个问题
最后返回结果是 len(stones) - uf.get_count(),count是连通分量的个数

每次union的时候，我们都是把两个点连通，所以连通分量的个数就会减少1
如果row, col从来没有出现过，就把当前的石头记录下来。

"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = {}, {}
        uf = UnionFind(len(stones))

        for i, (row, col) in enumerate(stones):
            if row in rows:
                uf.union(i, rows[row])
            else:
                rows[row] = i

            if col in cols:
                uf.union(i, cols[col])
            else:
                cols[col] = i
        
        return len(stones) - uf.get_count()