# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:42:32 2019

@author: Zhe Shen
"""

#Given the root to a binary tree, implement serialize(root), 
#which serializes the tree into a string, and 
#deserialize(s), which deserializes the string back into the tree.
#
#For example, given the following Node class
#
#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#The following test should pass:
#
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#        
def serialize(root):
    res = []
    res.append(root.val)
    
        
    if isinstance(root.left, Node):
        res.append(serialize(root.left))
        
    if (root.left == None):
        res.append('null')
            
        
    if isinstance(root.right, Node):
        res.append(serialize(root.right)) 
        
    if root.right == None:
        res.append('null')
    
    return res


#def deserialize(s):
    
node = Node('root', Node('left', Node('left.left')), Node('right'))
a = (serialize(node))
print(a)
#assert deserialize(serialize(node)).left.left.val == 'left.left'
