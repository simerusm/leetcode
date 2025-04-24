from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for ind, eq in enumerate(equations):
            graph[eq[0]][eq[1]] = values[ind]
            graph[eq[1]][eq[0]] = 1/values[ind]
        
        '''
        graph = {
            "a" = {"b": 2},
            "b" = {"a": 1/2, "c": 3},
            "c" = {"b": 1/3}
        }
        '''
      
        ans = []
        for query in queries:
            target = query[1]
            if query[0] not in graph or target not in graph:
                ans.append(-1.00000)
                continue

            q = deque([(query[0], 1)])
            seen = {query[0]}
            flag = False
            while q:
                currVar, currAns = q.popleft()
                if currVar == target:
                    ans.append(currAns)
                    flag = True
                    break
                for nextVar, multiplier in graph[currVar].items():
                    if nextVar not in seen:
                        q.append((nextVar, currAns * multiplier))
                        seen.add(nextVar)
            if not flag:
                ans.append(-1.00000)

        return ans

"""
- Implicit graph problem, it can be solved with DFS or BFS, used BFS to solve here
- This can be treated like a weighted graph, when given that a / b = 2, to traverse from a → b we can have a multiplier of 2 stating that a is 2 times bigger than b
  - Note that we want to handle the reciprocal relationship as well so we need to know that b / a = 1 /2
- Build a hashmap that stores a value to a dict as the key-value pair, we use a dict because a value can be considered for many equations such as a / c, a / b, a / d, etc…
  - This would all look like 
  - “A”: {“b”: val, “c”: val, “d”: val}
- Do a BFS on each of the queries and keep track of the multiplier as you go through
- Time complexity
  - O((V + E)*Q + EQ) 
    - where O(EQ) is the number of equations (edges essentially) for the initial graph pre processing
  - O(V + E) for worst case traversing all nodes connected to the starting node with BFS, where V is the number of variables (nodes) and E is the number of edges
    - Since you’re doing O(V + E) (worst case) search for each query, we multiply it by Q which represents the number of queries
- Space complexity
  - O(EQ + V)
  - When creating the graph worst case each equation is distinct thus having O(EQ) for the graph, where EQ is the number of equations
  - In BFS, at most the queue space will take up O(V) because you’ll be enqueuing all the vertices at a given node onto the queue to then deque and do more BFS on
"""
