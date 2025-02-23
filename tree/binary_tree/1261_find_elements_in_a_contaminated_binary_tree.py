from collections import deque 

class Node:
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.value = key 

class BinaryTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key) 
        else:
            self._insert(self.root, key)

    
    def _insert(self,current, key):
        if key < current.value:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)
        
    
    def inorder_traversal(self,node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self,node):
        if node:
            print(node.value, end="")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def dfs(self, node):
        if node:
            print(node.value, end=" ")
            self.dfs(node.left)
            self.dfs(node.right)

    def bfs(self):
        if self.root is None:
            return 
        
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


class FindElement:
    def __init__(self, root:Node):
        self.values = set()
        self._recover(root,0)

    def _recover(self, node:Node, val:int):
        if not node:
            return 
        node.val = val 
        self.values.add(val)
        self._recover(node.left , 2 * val + 1)
        self._recover(node.right, 2 * val + 2)
    
    def find(self, target:int)->bool:
        return target in self.values 
    

tree = BinaryTree()
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    tree.insert(val)

print("In-Order Traversal:")
tree.inorder_traversal(tree.root)
print("\nPre-Order Traversal:")
tree.preorder_traversal(tree.root)
print("\nPost-Order Traversal:")
tree.postorder(tree.root)

print("\n\nDFS (Pre-Order) Traversal:")
tree.dfs(tree.root)
print("\nBFS Traversal:")
tree.bfs()

node = Node(1)
find_elements = FindElement(node)

print(find_elements.find(-1))

