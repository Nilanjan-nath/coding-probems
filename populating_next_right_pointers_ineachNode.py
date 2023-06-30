'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.'''
class node:
    def __init__(self, data= 0 , left = None , right = None , next = None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

# In-order tree traversal (Left -> Root -> Right)
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)
# Pre-order tree traversal (Root -> Left -> Right)
def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)
# Post-order tree traversal (Left -> Right -> Root)
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

# # Creating a binary tree
# root = node(1)
# root.left = node(2)
# root.right = node(3)
# root.left.left = node(4)
# root.left.right =node(5)
# root.right.left =node(6)
# root.right.right = node(7)

# print("Binary Tree In-order Traversal:")
# inorder_traversal(root)
# print("\n")


# print("Binary Tree Post-order Traversal:")
# postorder_traversal(root)
# print("\n")
class Solution:
    def connect(self, root: 'node') -> 'node':
        if not root:
            return root
        
        # Start with the root node
        queue = [root]
        
        while queue:
            # Get the number of nodes in the current level
            size = len(queue)
            print(size)
            # Traverse through the nodes in the current level
            for i in range(size):
                # Get the first node from the queue
                node = queue.pop(0)
                print(queue)
                print(node.data)
                # If it's not the last node in the level, set its next to the next node in the queue
                if i < size - 1:
                    node.next = queue[0]
                
                # Add the node's children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # Return the root node
        return root
# Creating a binary tree
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right =node(5)
root.right.left =node(6)
root.right.right = node(7)
print("Binary Tree Pre-order Traversal:")
preorder_traversal(root)
print("\n")
s = Solution()
result_root = s.connect(root)
preorder_traversal(result_root)
print("\n")
