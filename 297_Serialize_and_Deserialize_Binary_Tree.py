# DFS: preorder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def rserialize(root, string):
            if root is None:
                string += 'None,'

            else:
                # we do preorder traversal here
                string += str(root.val) + ','
                string = rserialize(root.left,string)
                string = rserialize(root.right,string)
        
            return string 
        
        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def rdeserialize(l):
            
            if l[0] == 'None':
                l.pop(0)
                return None
            
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root
                        
        data_list = data.split(',')
        root = rdeserialize(data_list)
        
        return root 
    
       
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Time: O(N)
# Space:O(N)



# BFS 
class Codec:
    '''       O(n) time and O(n) space, BFS traversal
    e.g., 1
         / \
        2   5
       / \
      3   4  , level order traversal, serialize will be '1,2,5,3,4,None,None,None,None,None,None,'; deserialize 
      with queue as well, convert back. Time and Space O(n).
    '''
    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res
            
    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root

# Time: O(N)
# Space:O(N)


# More optimization on space:
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solution/


