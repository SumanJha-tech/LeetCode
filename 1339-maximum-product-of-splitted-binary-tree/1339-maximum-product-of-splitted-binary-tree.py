# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_prod = 0

        # 1️⃣ First DFS to calculate total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # 2️⃣ Second DFS to calculate subtree sums and max product
        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            subtree_sum = node.val + left_sum + right_sum
            
            # Try splitting here
            product = subtree_sum * (total - subtree_sum)
            self.max_prod = max(self.max_prod, product)
            
            return subtree_sum

        dfs(root)
        return self.max_prod % MOD
