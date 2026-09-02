class Solution(object):

    def inorderTraversal(self, root):
        result = []

        self.inOrder(root, result)

        return result

    def inOrder(self, root, result):

        if root is None:
            return

        self.inOrder(root.left, result)

        result.append(root.val)

        self.inOrder(root.right, result) 