# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        traverse_queue = deque([])
        startPath = destpath = ""

        traverse_queue.append((root, ""))

        while traverse_queue:
            node, path = traverse_queue.popleft()

            if startValue == node.val:
                startPath = path

            if destValue == node.val:
                destPath = path

            if node.left:
                traverse_queue.append((node.left, path + "L"))
            if node.right:
                traverse_queue.append((node.right, path + "R"))

        if startPath == "":
            return destPath

        startPosition = 0

        while startPosition < len(startPath) and startPosition < len(destPath) and startPath[startPosition] == destPath[startPosition]: 
            startPosition += 1

        return len(startPath[startPosition:]) * "U" + destPath[startPosition:]



