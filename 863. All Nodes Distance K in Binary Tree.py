class Solution:
    def convert_into_graph(self, node, parent, g):
        # To convert into graph we need to know who is the parent
        if not node:
            return
        
        if parent:
            g[node].append(parent)
            
        if node.right:
            g[node].append(node.right)
            self.convert_into_graph(node.right, node, g)
        
        if node.left:
            g[node].append(node.left)
            self.convert_into_graph(node.left, node, g)
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        g = defaultdict(list)
        vis, q, res = set(), deque(), []
        # We have a graph, now we can use simply BFS to calculate K distance from node.
        self.convert_into_graph(root, None, g)
        
        q.append((target, 0))
        
        while q:
            n, d = q.popleft()
            vis.add(n)
            
            if d == K:
                res.append(n.val)
            
            # adjacency list traversal
            for nei in g[n]:
                if nei not in vis:
                    q.append((nei, d + 1)) 
                
        return res

# Time: O(N)
# Space:O(N)



# V2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # build graph: graph consists of node as key with nei nodes as value 
        self.g = collections.defaultdict(list)
        self.convert_to_graph(root,None)
        
        # build queue to store node waitting to be visited 
        self.queue = collections.deque()
        self.visited = set()
        self.res = []
        
        # start from target node 
        self.queue.append((target,0))
        
        while self.queue:
            node,dist = self.queue.popleft()
            self.visited.add(node)
            
            if dist == K:
                self.res.append(node.val)
            
            for nei in self.g[node]:
                if nei not in self.visited:
                    self.queue.append((nei,dist+1))            
        
        return self.res 
        
    # build a graph first to make each node as key and 
    def convert_to_graph(self,node,parent):
        if not node:
            return 
        
        if parent:
            self.g[node].append(parent)
            
        if node.right:
            self.g[node].append(node.right)
            self.convert_to_graph(node.right,node)
        
        if node.left:
            self.g[node].append(node.left)
            self.convert_to_graph(node.left,node)
            
