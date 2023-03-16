# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs 
        
        # N L R - pre order

        # if leaf node:
            # if target done:
                # return True
            # else:
                # pop and continue
                
        def dfs(root, total):
            if not root:
                return False
            
            total += root.val
            if not root.left and not root.right:
                if total == targetSum:
                    return True
            left_found = dfs(root.left, total)
            right_found = dfs(root.right, total)
            
            if left_found or right_found:
                return True
            
            return False
            
        
        return dfs(root, 0)