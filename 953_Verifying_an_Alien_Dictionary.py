class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_indx = {}
        for idx,letter in enumerate(order):
            order_indx[letter] = idx 
        
        # compare adjacent words
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            # words that are the same can be skipped
            if word1 == word2:
                continue 
            
            # longer words, that start with the adjacent word, should not come first
            if len(word1)>len(word2):
                if word1.startswith(word2):
                    return False
            
            # compare each character, it must be smaller or equal to that of the                 adjacent word
            for k in range(min(len(word1),len(word2))):
                if order_indx[word1[k]]<order_indx[word2[k]]: 
                    break
                elif order_indx[word1[k]]==order_indx[word2[k]]: 
                    continue 
                else:
                    return False       
        return True 


# Time: O(C): C is total content of words
# Space:O(1)