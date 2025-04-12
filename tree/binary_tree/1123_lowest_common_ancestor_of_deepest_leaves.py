class TreeNode:
    def __init__(self, val, left=None, right=None):  # Default None set করাও ভালো
        self.val = val 
        self.left = left 
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)  # ✅ ঠিক করা নাম

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3)

sol = Solution()
lca = sol.lcaDeepestLeaves(root)
print(lca.val)