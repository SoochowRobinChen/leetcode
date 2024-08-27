class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        def dfs(index, label):
            labels[index] = label

            for nei in graph[index]:
                if labels[nei] == label:
                    return False
                
                if labels[nei] == 0 and not dfs(nei, -label):
                    return False
            return True 
        

        labels = [0] * len(graph)
        
        for i in range(len(graph)):
            if labels[i] == 0:
                if not dfs(i, 1):
                    return False
        
        return True 
