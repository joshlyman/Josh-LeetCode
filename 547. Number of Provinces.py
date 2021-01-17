class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

# different with number of islands, this is number of circles, elements of circles need not be all connected unlike in an "island", and have to build the visited set to check each element due to:
#         1001
#         0110
#         0111
#         1011

# here only len(isConnected) node exists, so need to search row and each nei node in matrix[node] 
        
        if not isConnected:
            return 0
    
        self.num = 0
        self.visited = set()
        
        nodeNum = len(isConnected)
        
        for i in range(nodeNum):
            if i not in self.visited:
                self.dfs(isConnected,i)
                self.num+=1
        
        return self.num 
        
    def dfs(self,isConnected,node):
        self.visited.add(node)
        
        for neind,neival in enumerate(isConnected[node]):
            if neival == 1 and neind not in self.visited:
                self.visited.add(neind)
                self.dfs(isConnected,neind)
                
        
# Time: O(NxN)
# Space:O(N)      
        
        
        
        