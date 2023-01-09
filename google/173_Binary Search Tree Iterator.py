# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
         # initialize list
        self.l = []

        # inorder nodes by asc
        self.inorder(root)

        # sort desc because pop(0) in O(k), k: length of list
        self.l = self.l[::-1]

    def inorder(self, root: Optional[TreeNode]):
        # exit condition
        if root == None:
            return
        
        # move to left node
        self.inorder(root.left)

        # add list
        self.l.append(root.val)

        # move to right node
        self.inorder(root.right)

    def next(self) -> int:
        # pop() in O(1)
        next_i = self.l.pop()
        return next_i

    def hasNext(self) -> bool:
        # get length in O(1)
        return len(self.l) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()