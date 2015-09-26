# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left is not None and root.right is not None: 
            node = self.find_rightest_node(root.left)
            node.right = root.right
            root.right = root.left
            root.left = None
            return
        if root.left is not None and root.right is None:
            root.right = root.left
            root.left = None
            return
    def find_rightest_node(self,root):
        tmp = root
        if tmp is None:
            return None
        while tmp.right is not None:
            if tmp.right is None:
                return tmp
            tmp = tmp.right
        return tmp
