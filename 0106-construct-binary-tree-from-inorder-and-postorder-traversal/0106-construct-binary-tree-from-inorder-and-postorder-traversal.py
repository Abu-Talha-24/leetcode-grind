# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # inorder   L N R
        # postorder L R N
        
        if not inorder or not postorder:
            return None
        
        rootval = postorder[-1]
        mid = inorder.index(rootval)
        root = TreeNode(rootval)
        
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root
        
        