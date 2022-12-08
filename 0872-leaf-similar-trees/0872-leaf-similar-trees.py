# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def get_leaf(n, v):
            if n.left:
                get_leaf(n.left, v)
                
            if n.right:
                get_leaf(n.right, v)
                
            if not (n.left or n.right) :
                v.append(n.val)
                
            return v

        return get_leaf(root1, []) == get_leaf(root2, [])

