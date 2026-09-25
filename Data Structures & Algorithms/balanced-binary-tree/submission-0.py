# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def get_depth(node):
            if not node:
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            if right_depth == -1 or left_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            return 1+max(left_depth, right_depth)
        if get_depth(root) == -1:
            return False
        return True
        