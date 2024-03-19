# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def tree(root):
            if not root: return []

            nodes = []

            def inorder(node):
                if node:
                    inorder(node.left)
                    nodes.append(node.val)
                    inorder(node.right)

            inorder(root)
            return nodes

        a = tree(root)
        return statistics.multimode(a)