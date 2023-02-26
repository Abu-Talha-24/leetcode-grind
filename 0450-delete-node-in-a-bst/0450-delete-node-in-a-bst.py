# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValNode(self, root: Optional[TreeNode]):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # minimum node from right subtree
                minVal = self.minValNode(root.right) # the value to be replaced with
                root.val = minVal # replace it
                root.right = self.deleteNode(root.right, minVal) # delete the replaced node
            
        return root
            
            
        
        