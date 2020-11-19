# similar with 560, in 560 we store diff between prefix sum and k as the key to count
# in 974, we store the mod between running sum and k  

class Solution:
    def subarraysDivByK(self, A, K):
		hmap,total,result = {},0,0
        for num in A:
            hmap[total] = hmap.get(total,0) + 1
            total += num
            total %= K
            if hmap.get(total):
                result += hmap[total]
        return result

class Solution:
    def subarraysDivByK(self, A, K):
        result,mod_map,running_sum = 0 ,{},0
        mod_map[0]=1
        for i in range(len(A)):
            running_sum+=A[i]
            if mod_map.get(running_sum%K) != None:
                val = mod_map.get(running_sum%K)
                result+=val
                mod_map[running_sum%K]=val+1
            else:
                mod_map[running_sum%K]=1
        return result



# V2

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        prefix = 0
        
        # store the remainder 
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res