# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  
        res = []
        q = deque()
        if root:
            q.append(root)
        
        while len(q) > 0:
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                if i == qLen-1: # last node at the end of the level
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
        
        
        
        
        