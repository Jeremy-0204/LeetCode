# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(root, s):
            s += f"{root.val}"

            if not root.right and not root.left:
                res.append(s)
                return
            
            if root.right:
                dfs(root.right, s + "->")
            if root.left:
                dfs(root.left, s + "->")
        
        dfs(root, "")
        return res