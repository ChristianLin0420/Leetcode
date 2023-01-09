class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        if n % 2 ==0:
            return []

        d = {}

        d[0] = [None]
        for i in range(1, n+1):
            d[i] = []

        for i in range(1, n+1):
            for li in range(i):
                left_len = li
                right_len = i - li - 1

                for left_node in d[left_len]:
                    for right_node in d[right_len]:
                        if left_node == None and right_node != None or left_node != None and right_node == None:
                            continue

                        d[i].append(TreeNode(0, left_node, right_node))

        return d[n]