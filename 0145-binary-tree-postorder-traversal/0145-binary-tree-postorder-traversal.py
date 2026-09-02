class Solution:
    def postorderTraversal(self, root):
        result = []

        def traversal(node):
            if node is None:
                return

            traversal(node.left)
            traversal(node.right)
            result.append(node.val)

        traversal(root)

        return result