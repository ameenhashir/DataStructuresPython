class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self,val):
        if self.data == val:
            return True

        if self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        #node
        elements.append(self.data)
        #right
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum += self.data
        if self.right:
            sum += self.right.calculate_sum()
        return sum

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [15,12,7,14,27,20,23,88 ]
    number_tree = build_tree(numbers)
    print('In order Traversal : ',number_tree.in_order_traversal())
    print('Pre order Traversal : ', number_tree.pre_order_traversal())
    print('Post order Traversal : ', number_tree.post_order_traversal())
    print('Is 33 exists in BST : ',number_tree.search(33))
    print('Is 33 exists in BST : ', number_tree.search(23))
    print('Max value : ', number_tree.find_max())
    print('Min value : ', number_tree.find_min())
    print('Value Sum : ',number_tree.calculate_sum())