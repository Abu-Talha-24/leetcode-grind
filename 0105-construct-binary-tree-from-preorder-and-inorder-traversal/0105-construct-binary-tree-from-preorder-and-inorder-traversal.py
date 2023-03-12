# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #preorder N L R
        #inorder L N R
        if not preorder or not inorder:
            return None
        
        root = preorder[0]
        mid = inorder.index(root)
        node = TreeNode(root)
        
        node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return node
        
        
        
        