class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        
        # s is empty 
        if idx == 4 and not s:
            # remove last '.'
            res.append(path[:-1])
            return 
        
        for i in range(1, len(s)+1):
            # cannot be 003 or 010
            # can be 0.0.0.0 
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)

# Time: O(C), because # of IP address is constant 
# Space:O(C)