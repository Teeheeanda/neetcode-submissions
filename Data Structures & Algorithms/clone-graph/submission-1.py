"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    clone_nodes = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        if self.clone_nodes.get(node, None):
            return self.clone_nodes[node]

        newNode = Node(node.val, [])
        self.clone_nodes[node] = newNode

        for n in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(n))      
        
        return newNode
    