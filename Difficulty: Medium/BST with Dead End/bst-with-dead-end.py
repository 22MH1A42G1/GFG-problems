class Solution:
    def isDeadEnd(self, root):
        # Code here
        queue = deque()
        queue.append(root)
        visited_nodes, leaf_nodes = set(), set()
        while queue:
            current_node = queue.popleft()
            visited_nodes.add(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            if not current_node.left and not current_node.right:
                leaf_nodes.add(current_node.data)
        for leaf in leaf_nodes:
            if (leaf == 1 and 2 in visited_nodes) or (leaf - 1 in visited_nodes and leaf + 1 in visited_nodes):
                return 1
        return 0