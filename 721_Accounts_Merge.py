# Introduction of Union Find
# https://www.youtube.com/watch?v=YKE4Vd1ysPI&ab_channel=%E9%BB%84%E6%B5%A9%E6%9D%B0 

# Union Find /Disjoint Set 
# https://www.youtube.com/watch?v=gpmOaSBcbYA&t=282s&ab_channel=%E9%BB%84%E6%B5%A9%E6%9D%B0

# Path expression for improving Union Find 
# https://www.youtube.com/watch?v=zos--xohLT0&ab_channel=%E9%BB%84%E6%B5%A9%E6%9D%B0 

# Python version 
# https://perper.site/2019/08/27/%E5%B9%B6%E6%9F%A5%E9%9B%86%EF%BC%8Cpython%E7%A4%BA%E4%BE%8B/

# Time complexity:
# MlogN
# Statement: If m operations, either Union or Find, are applied to n elements, 
# the total run time is O(m log*n), where log* is the iterated logarithm.
# https://en.wikipedia.org/wiki/Proof_of_O(log*n)_time_complexity_of_union%E2%80%93find

# Solution: Union Find, DFS, BFS  
# https://leetcode.com/problems/accounts-merge/discuss/721527/Easy-to-read-solutions-in-3-methods%3A-Union-Find-Graph-%2B-DFS-Graph-%2B-BFS


# Simple DFS
# https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!


# offical solution
# https://leetcode.com/problems/accounts-merge/solution/

# Uniond Find
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # DFS
        # For each account, draw the edge from the first email to all other emails. Additionally, we'll remember a map from emails to names on the side. After finding each connected component using a depth-first search, we'll add that to our answer.
        
        # Union Find 
        
        def find(x):
            if uf[x]!=x:
                uf[x]=find(uf[x])
            return uf[x]
        
        def union(x,y):
            idx,idy=find(x),find(y)
            if idx==idy:
                return 
            uf[idy]=idx 
                
        # creating union-find set of all unique emails.
        # All unique emails are keys and their values are their parent to which
        # they are attached in Union-find tree        
        uf={k:k for acc in accounts for k in acc[1:]}
        
        # clubing together all emails belonging to one person
        for acc in accounts:
            id_first=find(acc[1])
            for mail in acc[2:]:
                union(id_first,mail)
        
        # Extracting all emails under one set on union-find tree
        # Put them in a dictionary as list(emails) with key as their 'key' in UF tree
        hmap=defaultdict(list)
        for email in uf:
            hmap[find(email)].append(email)
        
        # Now, for any account, find 'key' of any of its email(here used 1st one) from UF tree
        # and fetch all emails associated under that key from 'hmap'. Put them sorted in 'ans'
        # and remove current 'key' from 'hmap' (because if key in hmap, than we will do above operation)
        ans=[]
        for acc in accounts:
            name=acc[0]
            uf_id=find(acc[1])
            if uf_id in hmap: # if current account has not been processed yet
                ans.append([name]+sorted(hmap[uf_id]))
                del hmap[uf_id]
        return ans


# Another version of Union Find
class DSU:
    def __init__(self):
        self.p = range(10001)
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


 # Time: O(AlogA), where A is the length of accounts[i]. If we used union-by-rank, this complexity improves to O(Aα(A))≈O(A), 
 # where alpha is the Inverse-Ackermann function.
 
 # Space: O(A), the space used by our DSU structure.


# DFS
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

