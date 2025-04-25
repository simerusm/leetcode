from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list) # n1: [(n2, color), (n3, color) ...]
        for redX, redY in redEdges:
            graph[redX].append((redY, 'R'))
        for blueX, blueY in blueEdges:
            graph[blueX].append((blueY, 'B'))

        res = [float('inf')] * n
        seen = {(0, None)}
        q = deque([(0, None, 0)]) # (node #, color, steps)
        while q:
            currNode, currColor, currSteps = q.popleft()

            res[currNode] = min(currSteps, res[currNode])

            for neighborNode, neighborColor in graph[currNode]:
                if neighborColor != currColor and (neighborNode, neighborColor) not in seen:
                    q.append((neighborNode, neighborColor, currSteps + 1))
                    seen.add((neighborNode, neighborColor))
        for x in range(n):
            if res[x] == float('inf'):
                res[x] = -1
        
        return res

"""
- Shortest path to a given node, since it’s unweighted we don’t need to use Dijikstra and we can just use BFS
- We first make a graph where each node contains neighbors and the color of the path required to travel to it (blue or red)
- We then initialize the data structures necessary for a BFS and our result array
- For the result array, initialize everything with infinity, it’s not that much overhead and it’s more overhead to store larger integer values than infinity actually
- In our queue and seen data structures, we want to add the first node to start our traversal, since we want to ensure we’re able to go over any of the edges starting from 0 and initialize the color of the starting nodes to be None as it’s guaranteed that it won’t be equal to blue or red when we do our check later on, so we’re able to traverse through all avenues from 0
- For the seen set, make sure not to store steps as well, here it’s not required because we’re always considered with the shortest path to a given node, and with BFS we’re guaranteed that and there’s no logic like with problem 1293. Shortest Path in a Grid with Obstacles Elimination where reaching a node in a certain amount of steps is going to lead to different paths/solutions
- On every queue pop, mark the respective node in the result array to be the min of the current steps taken and whatever value it had before in case the same node value can be reached again but from a different color pattern (one from red, one from blue)
- Loop through each neighbor of the current node and then only append it to the queue if the (neighbor node, neighbor color) combination isn’t seen already and if the current color isn’t equal to the neighbor color since we need to keep alternating
- At the end, you’ll have float(‘inf’)’s left over if you can’t reach certain nodes, so loop through res at the end and replace any infinities with -1
- States: 
  - Our states are (node, color) where each node can be visited at most 2 times.
  - Given that each state is a combination of a node and a color, the algorithm can visit each node twice (once for each color). 
  - Therefore, the number of possible states is the product of the ranges of each state variable:
  - Nodes: n possible nodes.
  - Colors: 2 possible colors.
- Time complexity:
  - Determined by the number of states and the operations performed for each state
  - Each node can be in 2 states (red or blue), so there are 2n states
  - For each state, we process all outgoing edges from that node (this is considered to be constant)
  - When forming the graph, we loop over the number of edges in blue and red, contributing to the time complexity
  - Thus it gives us a t.c. of O(n + e), where n is the number of states (nodes) and e is the number of edges
  - So we have O(n + e), N from the BFS and E from the initial pre-processing of the edge arrays when forming the graph, and the looping through neighbors of all the nodes will be O(e) because we had E edges, thus resulting in E neighbors in total to loop over
- Space complexity:
  - Graph: O(n + e)
  - Queue: O(n)
  - Seen set: O(n)
  - Result array: O(n)
  - Total: O(n + e), where n is the number of states and e is the number of edges
"""
