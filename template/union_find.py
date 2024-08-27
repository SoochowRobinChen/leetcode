class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[self.parent[x]]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] > self.rank[y_root]:
            self.rank[x_root] += self.rank[y_root]
            self.parent[y_root] = x_root
        else:
            self.rank[y_root] += self.rank[x_root]
            self.parent[x_root] = y_root
        
        return
    
    def size(self, x):
        return self.rank[self.find(x)]
