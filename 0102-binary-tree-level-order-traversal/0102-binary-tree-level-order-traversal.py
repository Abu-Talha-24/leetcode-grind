# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        
        if root:
            q.append(root)
            
        res = []
        
        while q:
            lvl = []
            for i in range(len(q)):
                root = q.popleft()
                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
                lvl.append(root.val)
            res.append(lvl)
        
        return res
        