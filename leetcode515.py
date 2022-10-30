from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

q = deque()

if root:
    q.append(root)
maximums = []

while q:
    rowVals = []
    for i in range(len(q)):
        node = q.popleft()
        rowVals.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    maximums.append(max(rowVals))
print(maximums)