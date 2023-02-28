# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder- N L R
        # inorder - L N R    
        if not preorder or not inorder:
            return None
        # first node of preorder is root
        root = TreeNode(preorder[0])
        # find root in inorder:
        mid = inorder.index(preorder[0])
        # left of inorder (till mid index) is left subtree and vice versa
        # (mid + 1) for preorder is the number of nodes in left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        