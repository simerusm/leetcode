from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        currRoads = set()

        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
            currRoads.add((connection[0], connection[1]))
        
        def dfs(node):
            nonlocal res
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in currRoads:
                        res += 1
                    
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = {0}
        dfs(0)
        return res
