# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(root, lower_range, upper_range):
            if not root:
                 return True
            elif lower_range<root.val<upper_range:
                return validate(root.left, lower_range, root.val) and validate(root.right, root.val, upper_range)
            else:
                return False
        return validate(root, float('-inf'), float('inf') )