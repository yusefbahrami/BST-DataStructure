class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, node: Node):
        temp = self.root
        while True:
            if not temp:
                self.root = node
                break
            elif node.data < temp.data:
                if temp.left == None:
                    temp.left = node
                    break
                else:
                    temp = temp.left
            elif node.data > temp.data:
                if temp.right == None:
                    temp.right = node
                    break
                else:
                    temp = temp.right

    # def recursiveInster(self, rootNode: Node, newNode: Node):
    #     if rootNode == None:
    #         self.root = newNode
    #         return rootNode
    #     elif newNode.data > rootNode.data:
    #         self.recursiveInster(rootNode.right, newNode)
    #     elif newNode.data < rootNode.data:
    #         self.recursiveInster(rootNode.left, newNode)

    def recursiveInster(self, rootNode: Node, newNode: Node):
        if rootNode == None:
            self.root = newNode
            return
        elif newNode.data > rootNode.data:
            if rootNode.right == None:
                rootNode.right = newNode
            else:
                self.recursiveInster(rootNode.right, newNode)
        elif newNode.data < rootNode.data:
            if rootNode.left == None:
                rootNode.left = newNode
            else:
                self.recursiveInster(rootNode.left, newNode)

    def inOrder(self, node: Node):
        if node:
            print(node.data)
            self.inOrder(node.left)
            self.inOrder(node.right)

    def preOrder(self, node: Node):
        if node:
            print(node.data)
            self.inOrder(node.right)
            self.inOrder(node.left)

    def find(self, data):
        temp = self.root
        while temp:
            if data == temp.data:
                return temp
            elif data > temp.data:
                temp = temp.right
            else:
                temp = temp.left
        return None

    def recursiveFind(self, data, node: Node):
        # if node == None:
        #     return None
        if data > node.data:
            if node.right is not None:
                return self.recursiveFind(data, node.right)
            else:
                return None
        elif data < node.data:
            if node.left is not None:
                return self.recursiveFind(data, node.left)
            else:
                return None
        elif data == node.data:
            return node

    def getBSTHeight(self, node: Node, rootNode: Node, h=0):
        if rootNode == None:
            h = -1
            return h
        if node is not None:
            if node.data > rootNode.data:
                return self.getBSTHeight(node, rootNode.right, h+1)
            elif node.data < rootNode.data:
                return self.getBSTHeight(node, rootNode.left, h+1)
            elif node.data == rootNode.data:
                return h

    def height(self, node: Node):
        if node is not None:
            left = self.height(node.left)
            right = self.height(node.right)
            return 1 + max(left, right)
        return -1


bst = BST()
n1 = Node(2)
n2 = Node(1)
n3 = Node(3)
n4 = Node(4)
n5 = Node(6)
n6 = Node(5)
# n7 = Node(5)

# bst.insert(n1)
# bst.insert(n2)
# bst.insert(n3)
# bst.insert(n4)
bst.recursiveInster(bst.root, n1)
bst.recursiveInster(bst.root, n2)
bst.recursiveInster(bst.root, n3)
bst.recursiveInster(bst.root, n4)
bst.recursiveInster(bst.root, n5)
bst.recursiveInster(bst.root, n6)
# bst.recursiveInster(bst.root, n7)
bst.inOrder(n1)
print("--------")
bst.preOrder(n1)
print("--------")
print(bst.find(3))
print(bst.find(7))
print("--------")
print(bst.recursiveFind(3, bst.root))
print(bst.recursiveFind(7, bst.root))
print("--------")
print(bst.getBSTHeight(n4, bst.root, 0))
print("--------")
print(bst.height(bst.root))
