# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        n = len(preorder)
        d = {postorder[i]:i for i in range(n)}

        for i in range(1,n):
            b = d[preorder[i]]

            while stack:
                a = d[stack[-1].val]
                if a - b > 0:
                    node = stack[-1]
                    new =  TreeNode(preorder[i])
                    if node.left == None:
                        node.left = new
                    else:
                        node.right = new
                    stack.append(new)
                    break
                else: 
                    stack.pop()

        return root