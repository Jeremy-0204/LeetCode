# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def visit(root):
            if not root:
                return
            
            self.count += 1
            visit(root.left)
            visit(root.right)
        
        visit(root)
        return self.count