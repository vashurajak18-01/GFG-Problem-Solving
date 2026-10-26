class Solution:
    def dfs(self, current_node, visited, path_vis, adj_list):
        visited[current_node] = 1
        path_vis[current_node] = 1
        for adj_node in adj_list[current_node]:
            if visited[adj_node] == 0:
                x = self.dfs(adj_node, visited, path_vis, adj_list)
                if x == True:
                    return True
            elif path_vis[adj_node] == 1:
                return True
        path_vis[current_node] = 0
        return False


    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        adj_list = [ [] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)

        visited = [0] * V
        path_vis = [0]* V
        for i in range(0, V):
            if visited[i] == 0:
                ans = self.dfs(i, visited, path_vis, adj_list)
                if ans == True:
                    return True
        return False