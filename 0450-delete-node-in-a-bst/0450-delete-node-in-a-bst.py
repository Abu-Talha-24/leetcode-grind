# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        def min_value(curr):
            # min value of of right sub tree
            while curr and curr.left:
                curr = curr.left
            return curr.val
        
        # find node - BST property
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                # minimum node from right subtree
                minVal = min_value(root.right) # the value to be replaced with
                root.val = minVal # replace it
                root.right = self.deleteNode(root.right, minVal) # delete the replaced node
            
        return root