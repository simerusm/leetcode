class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        from collections import defaultdict

        graph = defaultdict(list)
        # represent it being undirected
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            numberOfCon = 1
            for neighbor in graph[node]:
                if neighbor not in restricted and neighbor not in visited:
                    visited.add(neighbor)
                    numberOfCon += dfs(neighbor)
            return numberOfCon
        
        visited = {0}
        return dfs(0)

"""
- A graph DFS problem
- Have a visited set and then turn the restricted array into a set as well
- Starting from 0, DFS out on all the possible neighbors making sure the neighbor isn't in the restricted set and visited set
- In the dfs function keep track of the number of connections to the node we’re on
  - Have a variable to store the number of connections, initialize it to 1 at the start since one single node is still 1 connection
  - For each neighbor add their amount of connections to the current one
  - Then just return the number of connections of the node we’re on in the dfs call stack
- Return the function as it will get the number of connected nodes to 0
- Time complexity: O(n + e), where n is the number of nodes and e is the number of edges in the edges array. Essentially just O(n), worst case every single node is connected to 0 thus resulting in the dfs to go through every node
  - Converting restricted list to set: O(r) where r is the number of restricted nodes
  - Input processing: O(e) where e is the number of edges
  - Dfs: Worst case O(V+E) where E is the # of edges and V is # of vertices
    - The DFS function traverses each vertex once, marking it as visited.
    - For each vertex, it examines all its adjacent vertices (neighbors), which is essentially looping over the edges of a vertex
- Why DFS is O(V + E)
  - Vertices (V): Each vertex is visited once and only once. The DFS function ensures that each vertex is marked visited, and thus it will not be visited again.
  - Edges (E): For each vertex, DFS explores all its edges. In an adjacency list representation, iterating through all neighbors of a vertex (i.e., processing the edges connected to that vertex) is proportional to the number of edges.
- Space Complexity:
  - Graph Representation: The adjacency list representation requires O(V + E) space.
  - Visited Set: The visited set can contain at most V nodes, so O(V) space.
  - Recursion Stack: In the worst case, the recursion stack depth can be O(V) for a connected graph.
"""
