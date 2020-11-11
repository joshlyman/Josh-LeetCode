class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A)!=len(B) or set(A)!=set(B): #shouldnt even bother to swap 
            return False
        
        if A==B: #if A==B and all chars are unique so we cant swap we must have atleast 1 reapting char
            return False if len(set(A))==len(A) else True
        
        
        #A and B have the same length, and same chars in diff places lets try swap 
        firstMisMatch=0
        flagOk=0
        for a,b in zip(A,B):
            if a!=b and firstMisMatch==0:
                toSwapA=a
                toSwapB=b
                firstMisMatch=1 #first Mismatch found, time to find the 2nd
            elif a!=b and firstMisMatch==1: 
                if a==toSwapB and b==toSwapA and flagOk==0: #checking if the prev stored chars to swap are the same as the ones we have to swap and that this is the first swap (flagOk==0)
                    flagOk=1
                else:
                    return False #since we swapped before
        return True if flagOk==1 else False

# Time: O(N)
# Space:O(1)