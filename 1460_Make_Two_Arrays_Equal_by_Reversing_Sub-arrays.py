class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        return Counter(target) == Counter(arr)
            

# Time: O(N)
# Space:O(1)

def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

# Time: O(NlogN)
# Space:O(1)

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        countTarget = {}
        for i in target:
            if i in countTarget:
                countTarget[i]+=1
            else:
                countTarget[i]=1
           
        countArr = {}
        for i in arr:
            if i in countArr:
                countArr[i]+=1
            else:
                countArr[i]=1
        
        return countArr == countTarget

# Time: O(N)
# Space:O(N)