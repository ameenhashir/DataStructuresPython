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
                return self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        if self.data < data:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, data):
        if self.data == data:
            return True
        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.in_order_traversal()
        # node
        elements.append(self.data)
        # right
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        # node
        elements.append(self.data)
        # left
        if self.left:
            elements += self.left.pre_order_traversal()
        # right
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.post_order_traversal()
        # right
        if self.right:
            elements += self.right.post_order_traversal()
        # node
        elements.append(self.data)
        return elements

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def sum(self):
        sum = 0
        # node
        sum += self.data
        # left
        if self.left:
            sum += self.left.sum()
        # right
        if self.right:
            sum += self.right.sum()
        return sum

    def delete(self, data):
        if self.data > data:
            if self.left:
                self.left = self.left.delete(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self




def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4, 20, 1, 9, 18, 23, 34]
    number_tree = build_tree(numbers)
    print('In Order : ', number_tree.in_order_traversal())
    print('Pre Order : ', number_tree.pre_order_traversal())
    print('Post Order : ', number_tree.post_order_traversal())
    print("Find 20 : ", number_tree.search(20))
    print("Find Min : ", number_tree.find_min())
    print("Find Max : ", number_tree.find_max())
    print("Find Sum : ", number_tree.sum())
    number_tree.delete(17)
    print('Pre Order : ', number_tree.pre_order_traversal())
