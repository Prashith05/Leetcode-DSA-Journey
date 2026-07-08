"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # If the graph is empty
        if not node:
            return None

        # Dictionary to store:
        # original node -> cloned node
        visited = {}

        def dfs(current):

            # If already cloned, return the clone
            if current in visited:
                return visited[current]

            # Create a clone of the current node
            clone = Node(current.val)

            # Store it before exploring neighbors
            visited[current] = clone

            # Clone all neighbors
            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
        