class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        
        for w in words:
            if w not in d:
                d[w] = 1
            else:
                d[w] +=1
        
        # heap will sort the word with same freq in alphabetical order for tuple format 
        
        heap = []
        res = []
        import heapq 
        heapq.heapify(heap)
        
        for key in d:
            heapq.heappush(heap,(-d[key],key))
        
        for i in range(k):
            wtuple = heapq.heappop(heap)
            res.append(wtuple[1])
        
        return res

# Time: O(N+ k logN): N is length of words, count freq takes O(N) and add N words to heap, each takes O(logN) time. so pop k times will be klog(N)
# Space:O(N), store in dict will be O(N) space 