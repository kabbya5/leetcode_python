from typing import List 

class TreeNode:
    def __init__(self, value):
        self.val = value 
        self.left = None 
        self.right = None 

class Solution:
    def constructFromPrePost(self,preorder:List[int], postorder:List[int]):
        if not preorder or not postorder:
            return None 
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root 
        
        left_root_val = preorder[1] 
        left_subtree_size = postorder.index(left_root_val) + 1

        root.left = self.constructFromPrePost(preorder[1:left_subtree_size+1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size+1:], postorder[left_subtree_size:-1])

        return root
    

s = Solution()
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
root = s.constructFromPrePost(preorder, postorder)
print(root)  # 1
print(root.left.val, root.right.val)