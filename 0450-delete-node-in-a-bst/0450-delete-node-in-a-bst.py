# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.delete(root, key)
        
    def minNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val
    
    def delete(self, root, key):
        if not root:
            return root
        
        if key > root.val:
            root.right = self.delete(root.right, key)
        elif key < root.val:
            root.left = self.delete(root.left, key)
        else: # if found node
            if not root.left: 
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.minNode(root.right) 
                root.val = minVal
                root.right = self.delete(root.right, minVal)
        
        return root
                
