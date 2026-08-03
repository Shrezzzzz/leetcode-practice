class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        visited = {}  # maps original node -> cloned node
        
        def dfs(original):
            if original in visited:
                return visited[original]
            
            # Create the clone BEFORE recursing into neighbors,
            # so cycles don't cause infinite recursion
            clone = Node(original.val)
            visited[original] = clone
            
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)