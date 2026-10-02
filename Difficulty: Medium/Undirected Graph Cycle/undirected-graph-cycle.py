from collections import deque

class Solution:
    def isCycle(self, V, edges):
		#Code here
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0]*V
        for i in range(0, V):
            if visited[i] == 1:
                continue
            queue = deque()
            queue.append((i, -1))
            visited[i] = 1
            while len(queue) != 0:
                node, parent = queue.popleft()
                for adj_node in adj_list[node]:
                    if visited[adj_node] == 0:
                        visited[adj_node] = 1
                        queue.append((adj_node, node))
                    else:
                        if adj_node != parent:
                            return True
        return False