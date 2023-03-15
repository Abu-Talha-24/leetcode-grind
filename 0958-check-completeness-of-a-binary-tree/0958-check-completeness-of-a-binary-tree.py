# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        # level order traversal:
        
        q = []
        q.append(root)
        
        while q:
            lvl = []
            for i in range(len(q)):
                root = q.pop(0)
                if root == False:
                    lvl.append(False)
                    continue
                lvl.append(root.val)
                if root.left:
                    q.append(root.left)
                else:
                    q.append(False)
                if root.right:
                    q.append(root.right)
                else:
                    q.append(False)
            

            for i in range(len(lvl)):
                if lvl[i] == False:
                    if i == len(lvl) - 1 and not any(q):
                        return True
                    if any(lvl[i+1:]) == True:
                        return False
                    elif any(lvl[i+1:]) == False and any(q):
                        return False
                    else:
                        return True
                

        return True
                