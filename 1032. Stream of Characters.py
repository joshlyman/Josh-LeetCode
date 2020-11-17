# The problem is we don't know how many characters to match. On the example above, 
# should we try to match the last three stream characters "jkl", the last two "kl", or the last one "l"?

# The way to solve the problem is to notice that we always know the last character to match. 
# That gives us an idea to build a trie of reversed words, and try to match the reversed stream of characters.

# This way, instead of multiple choices to match, we always have one path: to match character by character 
# starting from the end of the stream. We could stop once we meet the "end of word" label, which means success. 
# If we couldn't match a character before we meet that label, that means fail.

# Trie is nested dict loop

# In this problem we need to reversed store char in trie and use deque to append left as reversed way to store words 

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])
        
        # because words might duplicate so we use set here 
        for word in set(words):
            node = self.trie 
            
            # need to store words in reversed way because we dont know when to start to match 
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                # if ch in node, so we go down to get the dict 
                node = node[ch]
            node['$'] = word
    
    # Time: O(NM), N is number of input words and M is word length
    # Space:O(NM)        
            
    def query(self, letter: str) -> bool:
        # we use deque here because it appendleft or addfirst using constant time 
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        # return True 
        return '$' in node 

    # Time: O(M), M is max word length, the depth of trie 
    # Space:O(M), to keep a stream of characters. One could limit the size of deque to be 
    # equal to the length of the longest input word.

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


