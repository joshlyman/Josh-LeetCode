# Complete solution
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.


# use startswith 
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
    Sort folders, so that parent will always occur in front of child
    For each folder, check if it starts with parent folder
    If it does, it's a subfolder, skip it. If not, make it next parent folder.
    """
        folders = folder

        folders.sort()
        output = []
        parent = ' '

        for folder in folders:
            if not folder.startswith(parent):
                output.append(folder)
                parent = folder + '/'

        return output

# Time: O(NlogN)
# Space:O(1), not count the output, if count, then O(N)

# trie 
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        Node = lambda: defaultdict(Node)
        trie = Node()
        
        ans = []
        for path in sorted(folder):
            n = trie
            for c in path[1:].split('/'):
                n = n[c]
                if '$' in n:
                    break
            else:
                n['$'] = True
                ans.append(path)
        return ans

# Time: O(NM)
# Space:O(1)