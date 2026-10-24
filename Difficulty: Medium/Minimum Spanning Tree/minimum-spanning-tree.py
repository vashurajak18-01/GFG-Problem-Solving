class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        adj = [[] for _ in range(V)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        mst = []
        total  = 0

        visited = [0 for _ in range(V)]
        priority_queue = []

        priority_queue.append([0, 0, -1])

        while len(priority_queue) != 0:
            wt, node, parent = heapq.heappop(priority_queue)
            if visited[node] == 0 :
                visited[node] = 1
                if parent != -1:
                    total += wt
                    mst.append([parent, node])
                for adjNode , wtt in adj[node]:
                    if visited[adjNode] == 0:
                        heapq.heappush(priority_queue, [wtt, adjNode, node])

        return total                
