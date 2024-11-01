# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
 

        arr1=[]
        valStr=""
        def node_traversal(node,valStr):
           
            if not node:
                return
            
            if valStr:
                valStr= valStr+"->"+str(node.val)
            else:
                valStr=str(node.val)
                    
            if not node.left and not node.right:
                arr1.append(valStr)
                return
            node_traversal(node.left,valStr)

            node_traversal(node.right,valStr)
                
        node_traversal(root,valStr)
        return arr1


