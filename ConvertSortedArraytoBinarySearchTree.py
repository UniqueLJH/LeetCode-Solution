# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nums = sorted(nums)
        lens = len(nums)
        if lens == 0:
            return None
        mid = lens/2
        leftnums = nums[0:mid]
        left = self.sortedArrayToBST(leftnums)
        rightnums = nums[mid+1:lens]
        right = self.sortedArrayToBST(rightnums)
        midnode = TreeNode(nums[mid])
        if left is not None:
            midnode.left = left
        if right is not None:
            midnode.right = right
        return midnode

if __name__ == "__main__":
    a = [7,6,5,4,3,2,1]
    S = Solution()
    n = S.sortedArrayToBST(a)
    print n.val
    print n.left.val
    print n.right.val
