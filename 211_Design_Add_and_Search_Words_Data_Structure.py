# use hashmap will take O(MxN) time. where MM is a length of the word to find, and NN is the number of words.

# Trie could use less space compared to hashmap when storing many keys with the same prefix. 
# In this case, using trie has only O(MxN) time complexity, where M is the key length, and N is the number of keys.

class WordDictionary:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        node = self.trie
        
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        
        # mark here means reach to end, if there is $ then word is found 
        node['$'] = True 
     
    # Time: O(M)
    # Space:O(M)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_node(word,node) -> bool:
            for i,ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.', check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            
                            # if x == $ that means it is already finished, so we dont need to move on 
                            if x!='$' and search_in_node(word[i+1:],node[x]):
                                return True 
                    
                    # if no node leads to answer or current ch is not '.', then word is not found 
                    return False 
                
                # if ch is found, go down to next level in trie 
                else:
                    node = node[ch]
            
            # return the word is found, which is True stored as $ in node 
            return '$' in node
        
    # Time: O(M), worst case is O(MxN) when word is underdefined (i.e. '.ig')
    # Space:O(1) for well-defined words, O(M) for underdefined words 
                
        return search_in_node(word, self.trie)         
                    
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)