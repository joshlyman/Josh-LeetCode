class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build a graph 
        self.g = collections.defaultdict(list)
        
        for edge in edges:
            edge0,edge1 = edge 
            
            if edge1 not in self.g[edge0]:
                self.g[edge0].append(edge1)
            
            if edge0 not in self.g[edge1]:
                self.g[edge1].append(edge0)
        
        self.visited = set()
        self.num = 0
        
        for i in range(n):
            if i not in self.visited:
                self.num+=1
                self.dfs(i)
        
        return self.num 
    
    def dfs(self,node):
        self.visited.add(node)

        for nei in self.g[node]:
            if nei not in self.visited:
                self.dfs(nei)
                
        
# Time: O(N)
# Space:O(N)