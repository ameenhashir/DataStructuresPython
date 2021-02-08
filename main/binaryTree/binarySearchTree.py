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
        elements = []
        #node
        elements.append(self.data)
        #left
        if self.left:
            elements += self.left.pre_order_traversal()
        #right
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
         #left
        if self.left:
            elements += self.left.pre_order_traversal()
        #right
        if self.right:
            elements += self.right.pre_order_traversal()
        # node
        elements.append(self.data)
        return elements


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print("In order traversal gives this sorted list:", country_tree.in_order_traversal())

    numbers_tree = build_tree([7, 12, 14, 15, 20, 23, 27, 88])
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:", numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:", numbers_tree.post_order_traversal())

    print('Min :' , numbers_tree.find_min())
    print('Max :' , numbers_tree.find_max())
    print('Sum :',numbers_tree.calculate_sum())