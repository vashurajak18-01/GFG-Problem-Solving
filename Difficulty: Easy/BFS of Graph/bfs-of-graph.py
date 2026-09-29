class Solution:
  
    
    def bfs(self, adj):
        n = len(adj)
        return self.bfs_algo(n, adj, 0)
        
    def bfs_algo(self, n, adj, start):
        
        ans = []                 
        visited = [0] * n        
        queue = deque([start])    
        visited[start] = 1

        while queue:
            e = queue.popleft()   
            ans.append(e)         

        
            for node in adj[e]:
                if visited[node] == 0:
                    visited[node] = 1
                    queue.append(node)

        return ans
