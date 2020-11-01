
from collections import defaultdict 
from random import choice 

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use array to store data 
        self.lst = []
        # use dict and set to store index of data 
        # set has add, del, update, remove operations to be able to use 
        self.idx = {}
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # add index of new data inside values' dict 
        index = len(self.lst)
        self.lst.append(val)
        
        if val not in self.idx:
            self.idx[val] = set([index])
            return True
        else:
            self.idx[val].add(index)
            return False
            
        
        # if already has, not 1, then return false 
        # return len(self.idx[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # if not contains, return false 
        if not self.lst or val not in self.idx:
            return False
        else:
            # get the removed value's index 
            idx_val = self.idx[val].pop()
            # get the last element 
            last = self.lst[-1]
            # get the index of last element
            idx_last = len(self.lst)-1

            # update list
            # put the last element in positon of removed value 
            self.lst[idx_val] = self.lst[idx_last]
            # then pop the last element
            self.lst.pop()

            # update dict 
            self.idx[last].add(idx_val)
            self.idx[last].remove(idx_last)

            # clear set of dict if it is empty
            if len(self.idx[val]) == 0:
                del self.idx[val]

            return True 

        
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        
        # return choice(self.lst)
        if len(self.lst) == 0: 
            return -1
        else: 
            return self.lst[random.randint(0, len(self.lst)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Use an array to store all element.
# Use a dictionary to store the appearane of each element. (key = val, value = set of index)

# To insert, simply add new element to the array and update the dictionary.
# To remove, first check the existance of this element with dictionary. (and get an arbitrary index)
# Swap it with the last element, and update the dictionary.
# To getRandom, directly use random.randint to get the index from the array.

import random

class RandomizedCollection(object):
    def __init__(self):
        self.collection = {}        # key = item stored in array, value = set of index
        self.array = []             # store all items in the array

    def insert(self, val):
        index = len(self.array)
        self.array += val,

        if val not in self.collection.keys():
            self.collection[val] = set([index])
            return True
        else:
            self.collection[val].add(index)
            return False

    def remove(self, val):
        if not self.array or val not in self.collection.keys():
            return False

        else:
            last = self.array[-1]                           # the other element
            i_last = len(self.array)-1                      # index of last position
            i_val = self.collection[val].pop()              # index of val position
            self.array[i_val] = self.array[i_last]          # update the array
            self.array.pop()

            self.collection[last].add(i_val)                # update the dict
            self.collection[last].remove(i_last)

            if len(self.collection[val]) == 0:
                del self.collection[val]                    # remove empty set
            
            return True

    def getRandom(self):
        if len(self.array) == 0: return -1
        else: return self.array[random.randint(0, len(self.array)-1)]

# Time: O(N)
# Space:O(N)
