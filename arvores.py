import matplotlib.pyplot as plt


import random


class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print (root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print (root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print (root.data)

    

           
    def inverse(self, root):
        if root is not None:
            # Swap the left and right subtrees
            root.left, root.right = root.right, root.left
            
            # Recursively invert the left and right subtrees
            self.inverse(root.left)
            self.inverse(root.right)
            
        return root
    
    def inverse_subtree(self, root, target_depth, current_depth=1):
        if root is not None:
            if current_depth == target_depth:
                # Swap the left and right subtrees at the target depth
                root.left, root.right = root.right, root.left
            else:
                # Recursively invert the left and right subtrees at deeper levels
                self.inverse_subtree(root.left, target_depth, current_depth + 1)
                self.inverse_subtree(root.right, target_depth, current_depth + 1)
        return root
    
    def navigate_and_inverse(self, root, position_sequence):
        node = root
        
        # Iterate through the position sequence
        for direction in position_sequence:
            if direction == 0 and node.left is not None:
                node = node.left
            elif direction == 1 and node.right is not None:
                node = node.right
        
        # Invert the subtree rooted at the selected node
        self.inverse(node)  # Assuming you want to start inversion from the selected node down
        
        return root
    
    # def _plot_node(self, ax, node, x=0, y=0, dx=1, dy=1):

    #     if (node.left) and (node.left):
    #         ax.plot([x, x - dx], [y, y - dy], 'k-')
    #         ax.text(x - dx*0.1, y, str(node.data), ha='center',
    #                 va='center', bbox=dict(facecolor='white', edgecolor='black'), rotation=25)

    #         self._plot_node(ax, node.left, x - dx, y - dy, dx*0.5, dy)

    #         ax.plot([x, x + dx], [y, y - dy], 'k-')
    #         ax.text(x + dx*0.1, y, str(node.data), ha='center',
    #                 va='center', bbox=dict(facecolor='white', edgecolor='black'), rotation=25)
    #         self._plot_node(ax, node.right, x + dx, y - dy, dx*0.5, dy)

        
    #     elif (node.left) and (node.right is None):
    #         ax.plot([x, x - dx], [y, y - dy], 'k-')
    #         ax.text(x - dx*0.1, y, str(node.data), ha='center',
    #                 va='center', bbox=dict(facecolor='white', edgecolor='black'), rotation=25)

    #         self._plot_node(ax, node.left, x - dx, y - dy, dx*0.5, dy)
            
    #     elif (node.left is None) and (node.right):
    #         ax.plot([x, x + dx], [y, y - dy], 'k-')
    #         ax.text(x + dx*0.1, y, str(node.data), ha='center',
    #                 va='center', bbox=dict(facecolor='white', edgecolor='black'), rotation=25)
    #         self._plot_node(ax, node.right, x + dx, y - dy, dx*0.5, dy)

    #     elif node.left is None and node.right is None:
    #         ax.text(x, y, str(node.data), ha='center', va='center',
    #                 bbox=dict(facecolor='white', edgecolor='black'))


            
    def _plot_node(self, ax, node, x=0, y=0, dx=2, dy=1):
        
        if node.left:
            ax.plot([x, x - dx], [y, y - dy], 'k-')
            ax.text(x , y, str(node.data), ha='center',
                    va='center', bbox=dict(facecolor='white', edgecolor='black'), rotation=25)

            self._plot_node(ax, node.left, x - dx, y - dy, dx*0.7, dy)

        if node.right:
            ax.plot([x, x + dx], [y, y - dy], 'k-')
            ax.text(x , y, str(node.data), ha='center',
                    va='center', bbox=dict(facecolor='white', edgecolor='black'), rotation=25)
            self._plot_node(ax, node.right, x + dx, y - dy, dx*0.7, dy)

        if node.left is None and node.right is None:
            ax.text(x, y, str(node.data), ha='center', va='center',
                    bbox=dict(facecolor='white', edgecolor='black'), rotation=25)

            
    def plot_tree(self, root):
        fig, ax = plt.subplots(figsize=(8, 6))
        self._plot_node(ax, root)
        plt.axis('off')
        
        return fig
        

        
    '''Cria uma árvore de maneira aleatoria, vai inseriendo um por vez'''



    def random_tree(self, size=42):
        values = random.sample(range(1, 1000), size)
        tree = Tree()
        root = None  # Initialize the root

        for v in values:
            root = tree.insert(root, v)  # Create and insert a Node with the value v

        return tree,root




            


def main():
    # root = None
    tree = Tree()
    # root = tree.insert(root, int(input("coloque a raiz: ")))
    # root = tree.insert(root, int(input("coloque un nodo: ")))
    # root = tree.insert(root, int(input("coloque un nodo: ")))
    # root = tree.insert(root, int(input("coloque un nodo: ")))
    # root = tree.insert(root, int(input("coloque un nodo: ")))
    # root = tree.insert(root, int(input("coloque un nodo: ")))
    # root = tree.insert(root, int(input("coloque un nodo: ")))

    # print ("\n Traverse Inorder")
    # tree.traverseInorder(root)
    # print ("\n Traverse Preorder")
    # tree.traversePreorder(root)
    # print ("\n Traverse Posorder")
    # tree.traversePostorder(root)


    # tree.plot_tree(root)
    # tree.plot_tree(tree.navigate_and_inverse(root,[0]))

    tree,root = tree.random_tree(4)
    tree.plot_tree(root)

    
    
   

if __name__ == "__main__":
    main()
