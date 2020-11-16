class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        # end of word 
        t['#'] = '#'
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        t = self.trie 
        for w in word:
            if w not in t:
                return False
            # go to next word 
            t = t[w]
        # find the end of word 
        if '#' in t:
            return True
        # means no '#' so it is not end of word, just prefix 
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie 
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        # we dont need to check '#': end of word
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Time: O(L) for insert, search and startswith, assume each word has length L
# Space:O(NL), store all words