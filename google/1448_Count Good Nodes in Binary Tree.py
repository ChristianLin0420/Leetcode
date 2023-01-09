# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, current_max):
            if not root:
                return

            if current_max <= root.val:
                self.count += 1
                current_max = root.val

            dfs(root.left, current_max)
            dfs(root.right, current_max)
        
        dfs(root, root.val)

        return self.count

            