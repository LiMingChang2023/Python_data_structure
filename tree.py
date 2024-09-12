class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):

        def insert_(root, value):
            if value > root.value:
                if root.right == None:
                    root.right = Node(value)
                    root.right.parent = root
                else:
                    insert_(root.right, value)

            else:
                if root.left == None:
                    root.left = Node(value)
                    root.left.parent = root
                else:
                    insert_(root.left, value)

        if self.root == None:
            self.root = Node(value)
            return
        insert_(self.root, value,)

    def get_min(self, root=None):
        if not root:
            root = self.root

        while root.left:
            root = root.left

        return root

    def get_max(self, root=None):
        if not root:
            root = self.root

        while root.right:
            root = root.right

        return root
            
    def delete(self, value):
        def check_child(node):
            if node.right == None and node.left == None:
                return 0
            elif node.right == None:
                return 1
            elif node.left == None:
                return 2
            else:
                return 3
                
        def delete_(node, value):
            if node == None:
                return
            parent = node.parent
            if node.value < value:
                delete_(node.right, value)
            elif node.value > value:
                delete_(node.left, value)
            
            else:
                if check_child(node) == 0:
                    if not parent:
                        self.root = None
                        del node
                    else:
                        if node.parent.rigtht == node:
                            node.parent.right = None
                        else:
                            node.parent.left = None

                        del node
                elif check_child(node) == 1:
                    if parent.left == node:
                        parent.left = node.left
                        node.left.parent = parent
                    else:
                        node.parent.right = node.left
                        node.left.parent = parent

                    del node
                elif check_child(node) == 2:
                    if parent.left == node:
                        parent.left = node.right
                        node.right.parent = parent
                    else:
                        parent.right = node.right
                        node.right.parent = parent
                else:
                    minNode = self.get_min(node)
                    node.value = minNode.value
                    delete_(minNode, minNode.value)

                    del node

        delete_(self.root, value)

        return
    
    def traversal(self, order):

        def traverse(root, order):
            if root == None:
                return
            if order == 'preorder':
                print(root.value)
                traverse(root.left, order)
                traverse(root.right, order)

            elif order == 'inorder':
                traverse(root.left, order)
                print(root.value)
                traverse(root.right, order)
            else:
                traverse(root.left, order)
                traverse(root.right, order)
                print(root.value)
        
        traverse(self.root, order)
                    

                
                
            
            
        
        

        
        