# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # level order 
        # print level[-1]
        res = []
        q = deque()
        if root:
            q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                level.append(root.val)
            res.append(level[-1])
        
        return res
                
        