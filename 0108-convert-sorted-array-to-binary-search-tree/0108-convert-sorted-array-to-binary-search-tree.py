# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return []
        
        def buildbinarytree(left,right):
            if left > right:
                return None

            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = buildbinarytree(left , mid-1)
            root.right = buildbinarytree(mid+1 , right)
            return root
        
        return buildbinarytree(0,len(nums)-1)
        
        
        