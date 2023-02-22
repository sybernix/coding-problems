class Solution:
    def __init__(self):
        self.min_diff = 100001
        self.prev_node = None

    def inOrderTraversal(self, root) -> int:
        if not root:
            return

        self.inOrderTraversal(root.left)

        if self.prev_node:
            self.min_diff = min(abs(root.val - self.prev_node.val), self.min_diff)

        self.inOrderTraversal(root.right)

    def minDiffInBST(self, root) -> int:
        return self.inOrderTraversal(root)