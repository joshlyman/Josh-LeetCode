class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        queue = collections.deque([[beginWord,1]])
        visited = set(beginWord)
        
        while queue:
            word,length = queue.popleft()
            if word == endWord:
                return length 
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz': 
                    new_word = word[:i] + c + word[i+1:]
                    # must be in dict and also cannot be visited before
                    if new_word not in wordList or new_word in visited:
                        continue 
                    queue.append([new_word,length+1])
                    visited.add(new_word)
        return 0 
            
                        
                    

Time: O(M^2 x N), where M is the length of words and N is the total number of words in the input word list.
Space:O(M^2 x N)