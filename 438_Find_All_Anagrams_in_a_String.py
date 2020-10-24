class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # use sliding window + hashmap, for each substring, use counter to store and compare with target substring 
        
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
            
            if scount[s[i-len(p)+1]] == 0:
                del scount[s[i-len(p)+1]]
        
        return output 
    
# Time: O(Ns + Np)
# Space:O(1)

Counter might be slow, if need to make a counter: 

class Solution:
    
    def makeCounter(self, s):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        return d
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counterP = self.makeCounter(p)
        counterI = self.makeCounter(s[:len(p)])
        result = []
        for i in range(0, len(s)-len(p)+1):
            if counterP == counterI:
                result.append(i)
            counterI[s[i]] -= 1
            if counterI[s[i]] == 0:
                del counterI[s[i]]
            if i + len(p) < len(s):
                counterI[s[i+len(p)]] = counterI.get(s[i+len(p)], 0) + 1 
        return result

                    
        
        
        
        
            
        
