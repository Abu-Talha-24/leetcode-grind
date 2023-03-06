# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        
        while True:
            while root: # Add all nodes to LEFT
                stack.append(root)
                root = root.left
            
            # Get NODE
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            # Go to RIGHT
            root = root.right
        