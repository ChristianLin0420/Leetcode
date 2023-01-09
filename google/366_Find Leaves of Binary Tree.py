class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node):
            if not node:
                return 0
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                m = max(l, r)

                for i in range(m + 1 - len(ans)):
                    ans.append([])
                
                ans[m].append(node.val)
                
                return m + 1

        dfs(root)

        return ans