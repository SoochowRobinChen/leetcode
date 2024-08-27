class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        """
        这一题跟 785 is graph bipartite 很像
        但是这一题是给定了n个人，然后给定了dislikes的关系
        然后要求将这n个人分成两组，使得每一组里面的人都不相互dislike

        都是用 dfs来解决，然后建立labels list 来记录每个人的label

        dfs(nei, -label) 如果false就返回false 
        """
        graph = [[] for _ in range(n + 1)]
        for dis in dislikes:
            graph[dis[0]].append(dis[1])
            graph[dis[1]].append(dis[0])

        labels = [0] * (n + 1)

        def dfs(index, label):
            labels[index] = label
            for nei in graph[index]:
                if labels[nei] == label:
                    return False
                if labels[nei] == 0 and not dfs(nei, -label):
                    return False
            
            return True
        
        for i in range(1, n + 1):
            if labels[i] == 0:
                if not dfs(i, 1):
                    return False
        return True 
