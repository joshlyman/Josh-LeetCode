class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letlogs = []
        diglogs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                diglogs.append(log)    
            else:
                letlogs.append(log)

        # if suffix is tie, sort by the letter 
        letlogs.sort(key=lambda x:x.split()[0])
        # sort the suffix 
        letlogs.sort(key=lambda x:x.split()[1:])
        
        return letlogs + diglogs 

# Time: O(M N logN), N is the number of logs in the list and M is the maximum length of a single log.
# Space:O(M N)