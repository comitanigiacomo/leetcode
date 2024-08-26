from platform import node
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def traverse(node):
            if node: 
                for children in node.children: 
                    traverse(children)
                    
                result.append(node.val)
                
        traverse(root)
        return result 