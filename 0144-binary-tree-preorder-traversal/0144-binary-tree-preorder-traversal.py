
class Solution(object):
    def preorderTraversal(self, root):
        result = []

        self.inOrder(root, result)

        return result

    def inOrder(self, root, result):

        if root is None:
            return
        result.append(root.val)    

        self.inOrder(root.left, result)

        self.inOrder(root.right, result)