class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n

        for _, y in edges:
            indegree[y] += 1
        
        return [node for node in range(n) if indegree[node] == 0]

"""
- An indegree graph problem
- The minimum number of vertices to reach all nodes are just the set of vertices that can’t be reached by any other nodes, therefore having an in-degree of 0 (no nodes go to this node)
- So, just create an in-degree array representing the indegree, or how many nodes point to the node we’re on, of every single node from 0 to n-1
- Return an array consisting of all the nodes that have an in-degree of 0
- Note:
  - Since it’s acyclic we don’t have to worry about an edge case
  - For a cycling graph, where it goes in a cycle, the indegree of each node is 1, but the minimum number of vertices is just one of the nodes
  - In our algorithm, we would return no nodes because each node has an in-degree of 1 but we need to return at least 1 node in the cycle to give the correct answer
  - This is an edge case to think about, but not something we have to worry about for this problem
- Time complexity: O(n + e), O(e) number of edges for first initial indegree making for loop and the O(n) checks each element in the in-degree array checking for indegrees of 0
- Space complexity: O(n), the space needed to store the in-degree array of n nodes
"""
