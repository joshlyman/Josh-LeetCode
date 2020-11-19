class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # use sliding window + hashmap, for each substring, use counter to 
        # store and compare with target substring 
        
        from collections import Counter 
        
        ns = len(s)
        np = len(p)
        
        if ns < np:
            return []
        
        pcount = Counter(p)
        
        # put first len(p)-1 chars inside counter 
        scount = Counter(s[:len(p)-1])
        
        output = []
        
        # start from len(p) th char, each time compare substring with target  
        for i in range(len(p)-1,ns):
            scount[s[i]]+=1
            
            if scount == pcount:
                output.append(i-len(p)+1)
            scount[s[i-len(p)+1]]-=1
            
            # make sure delete it if it is 0 
            if scount[s[i-len(p)+1]] == 0:
                del scount[s[i-len(p)+1]]
        
        return output 
    
      
        
        
        