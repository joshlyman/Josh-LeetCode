
# 3 pointers
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        i = j = k = 0

        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i, j, k = i+1, j+1, k+1
            elif arr1[i] < arr2[j]:
                i+=1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1

        return result

# Time: O(N)
# Space:O(1)

# HashMap 

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        combined = arr1 + arr2 + arr3
        get_dict = {}
        
        for x in combined:
            if x in get_dict:
                get_dict[x] += 1
            else:
                get_dict[x] = 1
        
        
        return sorted([key for key, val in get_dict.items() if val == 3])

# Time: O(NlogN)
# Space:O(N)

# V2
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        combined = arr1 + arr2 + arr3
        get_dict = {}
        
        for x in combined:
            if x in get_dict:
                get_dict[x] += 1
            else:
                get_dict[x] = 1
        
        res = []
        for key in get_dict:
            if get_dict[key] == 3:
                res.append(key)
        return sorted(res)
    