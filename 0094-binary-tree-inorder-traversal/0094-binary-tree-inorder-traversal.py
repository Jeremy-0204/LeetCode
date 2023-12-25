# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #values = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.printInorder(values, root)
        return values
    
    def printInorder(self, values, root):
        if root is None:
            return
        
        self.printInorder(values, root.left)
        
        values.append(root.val)
        
        self.printInorder(values, root.right)
        
#         if root is None: return
        
#         self.inorderTraversal(root.left)
#         self.values.append(root.val)
#         self.inorderTraversal(root.right)
        
#         answer = self.values[::]
#         print(self.values, answer)
#         self.values = []
#         return answer
        