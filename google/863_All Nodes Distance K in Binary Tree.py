# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)

        results = deque([target.val])
        visited_nodes = set([target.val])

        while results:
            if k == 0:
                return [node for node in results]
            for i in range(len(results)):
                node = results.popleft()
                for nei in graph[node]:
                    if nei not in visited_nodes:
                        visited_nodes.add(nei)
                        results.append(nei)
            k -= 1

        return []




