class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        status = [False]*len(s)
        final = ""
        for word in dict:
            start = s.find(word)
            last = len(word)

            # start is -1 means cannot find. if found, then make all index be True 
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True

                # find index of next word 
                start = s.find(word,start+1)
        i = 0
        i = 0
        # loop all s to add tag 
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final


# Time: O(N)
# Space:O(N)