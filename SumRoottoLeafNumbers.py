# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root:
            return 0
        
        output = []
        self.helper(root, 0, output)
        
        return sum(output)
        
    def helper(self, current, cursum, output):
        if not current:
            return []
        if not current.left and not current.right:
            output.append(cursum*10 + current.val)
            return
        
        cursum = cursum*10 + current.val
        
        self.helper(current.left, cursum, output)
        self.helper(current.right, cursum, output)
        
        
    
        
