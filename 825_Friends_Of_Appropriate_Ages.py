# For each pair (ageA, countA), (ageB, countB), if the conditions are satisfied with respect to age, then countA * countB pairs of people made friend requests.
# If ageA == ageB, then we overcounted: we should have countA * (countA - 1) pairs of people making friend requests instead, as you cannot friend request yourself.

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0]*121
        
        for age in ages:
            count[age]+=1
        
        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: 
                    continue
                if ageA < ageB: 
                    continue
                if ageA < 100 < ageB: 
                    continue
                    
                ans+= countA*countB
                if ageA == ageB:
                    ans -= countA
        
        return ans 

# Time: O(A^2+N), where N is the number of people, and A is the number of ages.
# Space:O(A)