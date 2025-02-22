class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
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

"""
- Graph problem
- The trick here is to not actually reorder everything, it’s just to count how many roads are out of place
- Any road that is pointing away from 0 needs to be switched around
- Make sure when pre-processing and making a graph structure, to make it bi-directional to ensure you can reach every node from 0
- Also, make sure to create a set of the connections that were given originally for O(1) checking
- Do DFS starting from node 0 and essentially reach the end of all its possible neighbors and see at what times the road is pointing away from 0 by checking to see if, for the current node, the neighbor is not in seen and if (curr node, neighbor) exists in the set of connections that we created during pre-processing, then it's pointing away from 0 and must switch directions, thus incrementing 1 to the result
- Time complexity: O(n), we visit every node at most once and the graph pre-processing is edge-based so it will be O(n) to iterate through
- Space complexity: O(n), number of edges is n - 1 = O(n). All the other stuff like graphs and the current roads take up at most O(n) as well
"""
