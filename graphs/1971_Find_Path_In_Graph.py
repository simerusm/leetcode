class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        seen = {source}
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        dfs(source)

        if destination not in seen:
            return False
        return True

"""
- This is a basic DFS graph problem
- Create the bidirectional graph hash map
- Dfs starting from the source, once the dfs finishes and all the possible nodes that can be visited starting from the source have been added to a seen set, if the destination node is in this seen set return True as it can be reached, otherwise false
- Time complexity: O(n + e) where e represents the number of edges and n represents the number of nodes/vertices (worst case)
- Space complexity: O(n + e), same declarations as above
"""
