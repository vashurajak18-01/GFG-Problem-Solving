class Solution:
    def dfs(self, current_node, visited, stack, adj):
        visited[current_node] = 1

        for adj_node in adj[current_node]:
            if visited[adj_node] == 0:
                self.dfs(adj_node, visited, stack, adj)
        stack.append(current_node)

    def topoSort(self, adj: list[list[int]]) -> list[int]:
        # code here
        V = len(adj)
        visited = [0] * V
        stack = []

        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, visited, stack, adj)
        return stack[::-1]
        